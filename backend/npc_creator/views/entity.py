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
from npc_creator.models.collection import Collection
from npc_creator.models.entities.custom import Custom
from npc_creator.models.entities.npc import Npc
from npc_creator.models.entities.location import Location
from npc_creator.models.favorite import Favorite
from npc_creator.models.image_generation import ImageGeneration


from rest_framework import serializers, viewsets, status

from npc_creator.views.image import ImageSerializer


class EntitySerializer(serializers.ModelSerializer):
    image_objects = ListSerializer(child=ImageSerializer())
    id = serializers.SerializerMethodField("get_uuid_as_id")
    collections = serializers.SerializerMethodField("get_requested_user_collections")

    class Meta:
        model = Entity
        fields = [
            "id",
            "state",
            "kind",
            "image_generator_description",
            "image_objects",
            "values",
            "collections",
        ]

    def get_uuid_as_id(self, obj):
        return obj.uuid

    def get_requested_user_collections(self, obj):
        request = self.context.get("request", None)
        if request is not None and request.user.is_authenticated:
            user = request.user

            return [
                c.name
                for c in Collection.objects.filter(
                    user=user, favorites__entity_id=obj.id
                )
            ]

        return []


ENTITIES_CLASSES = {
    "npc": Npc,
    "npcs": Npc,
    "location": Location,
    "locations": Location,
    "custom": Custom,
    "customs": Custom,
}


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.order_by("-created_at")
    serializer_class = EntitySerializer

    permission_classes = []

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        if str(self.kwargs["pk"]).isdigit():
            namespace_uuid = uuid.UUID("12345678-1234-5678-1234-567812345678")
            self.kwargs["pk"] = uuid.uuid5(namespace_uuid, self.kwargs["pk"])
        obj = get_object_or_404(queryset, uuid=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)

        obj = obj.instance

        if "schema" in self.request.query_params:
            obj.Fill(entity=obj, schema=self.request.query_params["schema"]).call()

        obj.refresh_from_db()

        return obj

    def get_queryset(self):
        if self.action == "list":
            queryset = self.queryset

            own = self.request.query_params.get("own", False)
            favorites = self.request.query_params.get("favorites", False)
            if own:
                queryset = queryset.filter(creator=self.request.user)
            elif favorites:
                queryset = queryset.filter(favorite__collection__user=self.request.user)
                queryset = queryset.order_by("-favorite__created_at")
            else:
                queryset = queryset.filter(state=Entity.States.PUBLISHED)

            kinds = self.request.query_params.getlist("kind[]", [])
            queryset = queryset.filter(kind__in=kinds)

            search_text = self.request.query_params.get("search", "").strip()
            regex = f"(^|[^A-Za-z]){search_text}([^A-Za-z]|$)"

            return queryset.filter(attributes__iregex=regex).distinct()
        return self.queryset

    @action(detail=False, methods=["get"])
    def random(self, request):
        entity = self.queryset.order_by("?").first()
        return Response(self.serializer_class(entity).data)

    def update(self, request, *args, **kwargs):
        data = request.data

        id = data.get("id")
        entity = Entity.objects.get(uuid=id).instance

        if entity.state == Entity.States.UNPUBLISHED:
            entity.add_values(data.get("values"))
            entity.state = Entity.States.PUBLISHED
            entity.save()

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

        entity = ENTITIES_CLASSES[data.get("kind")]()
        entity.prompt = prompt
        result = entity.Fill(entity=entity).call()
        if not result:
            return Response({"type": "error", "error": result.error})

        if not result:
            return Response(
                {"type": "error", "error": "custom", "message": result.error}
            )

        if request.user.is_authenticated:
            entity.creator = request.user
        entity.save()
        generation = ImageGeneration(entity=entity)
        generation.save()
        generation_job_async(generation)

        return Response(
            {"type": "success", "entity": self.serializer_class(entity).data}
        )

    @action(detail=True, methods=["patch"])
    def favorite(self, request, pk):
        if request.user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        data = json.loads(request.body.decode())
        favorite = bool(data.get("favorite"))

        entity = self.get_object()

        collection, _ = Collection.objects.get_or_create(
            user=request.user, name="favorite"
        )

        if favorite:
            Favorite.objects.get_or_create(entity=entity, collection=collection)
        elif not favorite:
            collection.favorites.filter(entity=entity).delete()
        return Response()

    @action(detail=True, methods=["post"])
    def recreate_images(self, request, pk):
        return
        entity = self.queryset.get(pk=pk)

        generation = ImageGeneration(entity=entity)
        generation.save()
        generation_job_async(generation)

        time.sleep(random.random() + random.randint(3, 10))

        return Response(
            {"type": "success", "entity": self.serializer_class(entity).data}
        )
