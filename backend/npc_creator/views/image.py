import rest_framework_simplejwt
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
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
from npc_creator.models.image import Image
from npc_creator.models.image_generation import ImageGeneration
from npc_creator.operations.generate_npc import GenerateNpc
from npc_creator.repositories import npc_repo

from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from npc_creator.models import Entity
from rest_framework import serializers, viewsets


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "name", "score"]


class ImageViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]

    queryset = Image.objects.prefetch_related().all()
    serializer_class = ImageSerializer

    @action(detail=True, methods=["post"], authentication_classes=[JWTAuthentication])
    def upvote(self, request, pk):
        image = Image.objects.filter(id=pk)[0]
        template = image.template

        image.upvote()
        image.save()
        if template:
            template.upvote()
            template.save()
        return Response({"type": "success"})

    @action(detail=True, methods=["post"], authentication_classes=[JWTAuthentication])
    def downvote(self, request, pk):
        image = Image.objects.filter(id=pk)[0]
        template = image.template

        image.downvote()
        image.save()
        if template:
            template.downvote()
            template.save()
        return Response({"type": "success"})
