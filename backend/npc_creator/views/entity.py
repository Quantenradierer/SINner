import random
import time
import uuid
from datetime import timedelta
from time import sleep

import rest_framework.permissions
from django.core.cache import cache
from django.utils.timezone import now
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.serializers import ListSerializer
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
import json

from npc_creator.jobs.generation_job import generation_job_async
from npc_creator.models import Entity
from npc_creator.models.entities.custom import Custom
from npc_creator.models.entities.npc import Npc
from npc_creator.models.entities.location import Location
from npc_creator.models.image_generation import ImageGeneration


from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from rest_framework import serializers, viewsets

from npc_creator.views.image import ImageSerializer


class EntitySerializer(serializers.ModelSerializer):
    image_objects = ListSerializer(child=ImageSerializer())
    id = serializers.SerializerMethodField("get_uuid_as_id")

    class Meta:
        model = Entity
        fields = [
            "id",
            "image_generator_description",
            "image_objects",
            "values",
        ]

    def get_uuid_as_id(self, obj):
        return obj.uuid


class GenericEntityView(viewsets.ModelViewSet):
    entity_class = None
    queryset = None
    serializer_class = EntitySerializer

    authentication_classes = [rest_framework.authentication.TokenAuthentication]
    permission_classes = []

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        if str(self.kwargs["pk"]).isdigit():
            namespace_uuid = uuid.UUID("12345678-1234-5678-1234-567812345678")
            self.kwargs["pk"] = uuid.uuid5(namespace_uuid, self.kwargs["pk"])
        obj = get_object_or_404(queryset, uuid=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)

        if "schema" in self.request.query_params:
            self.entity_class().Fill(
                entity=obj, schema=self.request.query_params["schema"]
            ).call()

        obj.refresh_from_db()

        return obj

    def get_queryset(self):
        search_text = self.request.query_params.get("search", "").strip()

        regex = f"(^|[^A-Za-z]){search_text}([^A-Za-z]|$)"
        return self.queryset.filter(attributes__iregex=regex).distinct()

    @action(detail=False, methods=["get"])
    def random(self, request):
        entity = self.queryset.order_by("?").first()
        return Response(self.serializer_class(entity).data)

    @action(detail=False, methods=["post"])
    def prompt(self, request):
        data = json.loads(request.body.decode())

        prompt = data.get("prompt")
        if not prompt:
            return Response(
                {
                    "type": "error",
                    "error": "Zum ausfüllen musst du einen Prompt eingeben.",
                }
            )

        prompt = prompt[:255]

        entity = self.entity_class()
        entity.prompt = prompt
        result = self.entity_class.Fill(entity=entity).call()
        if not result:
            return Response({"type": "error", "error": result.error})

        if not result:
            return Response(
                {"type": "error", "error": "custom", "message": result.error}
            )

        entity.save()
        generation = ImageGeneration(entity=entity)
        generation.save()
        generation_job_async(generation)

        return Response(
            {"type": "success", "entity": self.serializer_class(entity).data}
        )

    @action(detail=True, methods=["post"], authentication_classes=IsAuthenticated)
    def recreate_images(self, request, pk):
        entity = self.queryset.get(pk=pk)

        for i in range(10):
            generation = ImageGeneration(entity=entity)
            generation.save()
            generation_job_async(generation)

            time.sleep(random.random() + random.randint(3, 10))

        return Response(
            {"type": "success", "entity": self.serializer_class(entity).data}
        )


class NpcViewSet(GenericEntityView):
    entity_class = Npc
    queryset = Npc.objects.order_by("-created_at")


class LocationViewSet(GenericEntityView):
    entity_class = Location
    queryset = Location.objects.order_by("-created_at")


class CustomViewSet(GenericEntityView):
    entity_class = Custom
    queryset = Custom.objects.order_by("-created_at")
