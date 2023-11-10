import datetime
import random
import time
from datetime import timedelta
from string import ascii_uppercase
from time import sleep

import rest_framework_simplejwt
from django.core.cache import cache
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from rest_framework.serializers import ListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
)
import json

from rest_framework_simplejwt.authentication import JWTAuthentication

from npc_creator import config
from npc_creator.jobs.generation_job import generation_job_async
from npc_creator.models.gpt_request import GptRequest
from npc_creator.models.image_generation import ImageGeneration
from npc_creator.operations.generate_npc import GenerateNpc
from npc_creator.operations.gpt.alternative_attributes import AlternativeAttributes
from npc_creator.operations.gpt.check_npc import CheckNpc
from npc_creator.repositories import npc_repo

from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from npc_creator.models import Npc, Attribute
from rest_framework import serializers, viewsets

from npc_creator.views.image import ImageSerializer


class NpcSerializer(serializers.ModelSerializer):
    attributes = serializers.DictField()
    image_objects = ListSerializer(child=ImageSerializer())

    class Meta:
        model = Npc
        fields = [field.name for field in Npc._meta.fields] + [
            "attributes",
            "image_objects",
        ]


class NpcViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]

    queryset = Npc.objects.order_by("-id").prefetch_related().all()
    serializer_class = NpcSerializer

    def get_queryset(self):
        search_text = self.request.query_params.get("search", "")

        regex = f"(^|[^A-Za-z]){search_text}([^A-Za-z]|$)"
        return self.queryset.filter(attribute__value__regex=regex).distinct()

    @action(detail=False, methods=["get"])
    def random(self, request):
        npc = npc_repo.read_random()
        return Response(NpcSerializer(npc).data)

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def prompt(self, request):
        data = json.loads(request.body.decode())
        prompt = data.get("prompt")[:255]

        serializer = self.get_serializer(data=data.get("npc", None))

        if serializer.is_valid(raise_exception=True):
            npc = Npc(attributes=serializer.validated_data["attributes"])

            result_npc = GenerateNpc(prompt, npc).call()
            if result_npc:
                return Response(
                    {"type": "success", "npc": NpcSerializer(result_npc.data).data}
                )
            else:
                return Response({"type": "error", "error": result_npc.error})

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def save(self, request):
        data = json.loads(request.body.decode())

        serializer = self.get_serializer(data=data.get("npc", None))

        if serializer.is_valid(raise_exception=True):
            npc = Npc(attributes=serializer.validated_data["attributes"])

            if npc.is_complete():
                result = CheckNpc(npc=npc).call()

                if not result:
                    return Response(
                        {"type": "error", "error": "custom", "message": result.error}
                    )

                npc.save()
                generation = ImageGeneration(npc=npc)
                generation.save()
                generation_job_async(generation)

                return Response({"type": "success", "npc": NpcSerializer(npc).data})
        return Response({"type": "error", "error": "npc_incomplete"})

    @action(detail=True, methods=["post"], authentication_classes=[JWTAuthentication])
    def recreate_images(self, request, pk):
        npc = npc_repo.find(pk)

        for i in range(10):
            if (
                ImageGeneration.objects.filter(
                    url__isnull=True, created_at__gt=now() + timedelta(hours=-1)
                ).count()
                < 10
            ):
                generation = ImageGeneration(npc=npc)
                generation.save()
                generation_job_async(generation)

            time.sleep(random.random() + random.randint(3, 10))

        return Response({"type": "success", "npc": NpcSerializer(npc).data})

    @action(detail=True, methods=["post"], authentication_classes=[JWTAuthentication])
    def set_default_image(self, request, pk):
        npc = npc_repo.find(pk)
        npc.default_image_number = int(request.data["image_number"])
        npc_repo.save(npc)
        return Response({"type": "success", "npc": NpcSerializer(npc).data})

    @action(detail=True, methods=["post"], permission_classes=[AllowAny])
    def alternatives(self, request, pk):
        npc = npc_repo.find(pk)

        data = json.loads(request.body.decode())
        attribute = data.get("attribute", None)

        if attribute not in npc.attributes:
            return Response({"type": "error", "error": "TODO"})

        key = f"AlternativeAttributes-npc{npc.id}-{attribute}"
        for i in range(600):
            result = cache.get(key)
            if not result:
                break
            sleep(0.1)

        if not npc.attribute_set.filter(generation__gt=0, key=attribute).exists():
            cache.set(key, "True")
            result = AlternativeAttributes(npc=npc, attribute=attribute).call()
            for alternative in result.data:
                Attribute.objects.create(
                    npc=npc, key=attribute, value=alternative, generation=1
                )
            cache.delete(key)

        attributes = npc.attribute_set.filter(generation__gt=0, key=attribute)
        if attributes:
            return Response(
                {"type": "success", "alternatives": [attr.value for attr in attributes]}
            )

        return Response({"type": "error", "error": "TODO"})
