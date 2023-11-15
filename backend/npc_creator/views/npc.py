import datetime
import random
import time
from datetime import timedelta
from string import ascii_uppercase
from time import sleep

import rest_framework_simplejwt
from django.core.cache import cache
from django.db.migrations.serializer import DictionarySerializer
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
from npc_creator.models import Entity
from npc_creator.models.entities.npc import Npc
from npc_creator.models.entities.location import Location
from npc_creator.models.image_generation import ImageGeneration
from npc_creator.operations.generate_location import GenerateLocation
from npc_creator.operations.generate_npc import GenerateNpc
from npc_creator.operations.gpt.alternative_attributes import AlternativeAttributes
from npc_creator.operations.gpt.check_npc import CheckNpc

from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from rest_framework import serializers, viewsets

from npc_creator.views.image import ImageSerializer



class EntitySerializer(serializers.ModelSerializer):
    image_objects = ListSerializer(child=ImageSerializer())

    class Meta:
        model = Entity
        fields = [
            "id",
            "primary_values",
            "image_generator_description",
            "image_objects",
            "attribute_definition"
        ]

class GenericEntityView(viewsets.ModelViewSet):
    entity_class = None
    queryset = None
    serializer_class = EntitySerializer

    GenerationOperation = None


    authentication_classes = [BasicAuthentication, SessionAuthentication]
    def get_queryset(self):
        search_text = self.request.query_params.get("search", "")

        regex = f"(^|[^A-Za-z]){search_text}([^A-Za-z]|$)"
        return self.queryset.filter(attributes__regex=regex).distinct()

    @action(detail=False, methods=["get"])
    def random(self, request):
        entity = self.queryset.order_by("?").first()
        return Response(self.serializer_class(entity).data)

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def prompt(self, request):
        data = json.loads(request.body.decode())
        prompt = data.get("prompt")[:255]
        values = data.get("values")

        entity = self.entity_class()
        entity.add_values(values)
        result_entity = self.GenerationOperation(prompt, entity).call()
        if result_entity:
            return Response(
                {"type": "success", "entity": self.serializer_class(result_entity.data).data}
            )
        else:
            return Response({"type": "error", "error": result_entity.error})

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def save(self, request):
        data = json.loads(request.body.decode())
        values = data.get("values")

        entity = self.entity_class()
        entity.add_values(values)

        if not entity.is_complete():
            return Response({"type": "error", "error": "npc_incomplete"})
        result = CheckNpc(npc=entity).call()

        if not result:
            return Response(
                {"type": "error", "error": "custom", "message": result.error}
            )

        entity.save()
        generation = ImageGeneration(entity=entity)
        generation.save()
        generation_job_async(generation)

        return Response({"type": "success", "entity": self.serializer_class(entity).data})

    @action(detail=False, methods=["get"], permission_classes=[AllowAny])
    def default(self, request):
        return Response({"type": "success", "entity": self.serializer_class(self.entity_class()).data})

    @action(detail=True, methods=["post"], authentication_classes=[JWTAuthentication])
    def recreate_images(self, request, pk):
        entity = self.queryset.get(pk=pk)

        for i in range(10):
            if (
                ImageGeneration.objects.filter(
                    url__isnull=True, created_at__gt=now() - timedelta(hours=-1)
                ).count() < 10
            ):
                generation = ImageGeneration(entity=entity)
                generation.save()
                generation_job_async(generation)

            time.sleep(random.random() + random.randint(3, 10))

        return Response({"type": "success", "entity": self.serializer_class(entity).data})

    @action(detail=True, methods=["post"], permission_classes=[AllowAny])
    def alternatives(self, request, pk):
        npc = npc_repo.find(pk)

        data = json.loads(request.body.decode())
        attribute = data.get("attribute", None)

        if attribute not in npc.primary_values:
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


class NpcViewSet(GenericEntityView):
    entity_class = Npc
    queryset = Npc.objects.order_by("-id")

    GenerationOperation = GenerateNpc


class LocationViewSet(GenericEntityView):
    entity_class = Location
    queryset = Location.objects.order_by("-id").all()

    GenerationOperation = GenerateLocation
