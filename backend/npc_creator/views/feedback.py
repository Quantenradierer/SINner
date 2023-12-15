import random
import time
from datetime import timedelta
from time import sleep

from django.core.cache import cache
from django.utils.timezone import now
from rest_framework.decorators import action
from rest_framework.serializers import ListSerializer
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
)
import json

from rest_framework_simplejwt.authentication import JWTAuthentication

from npc_creator.jobs.generation_job import generation_job_async
from npc_creator.models import Entity
from npc_creator.models.entities.custom import Custom
from npc_creator.models.entities.npc import Npc
from npc_creator.models.entities.location import Location
from npc_creator.models.feedback import Feedback
from npc_creator.models.image_generation import ImageGeneration
from npc_creator.operations.gpt.alternative_attributes import AlternativeAttributes


from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from rest_framework import serializers, viewsets, mixins

from npc_creator.views.image import ImageSerializer


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ["email", "comment"]


class FeedbackViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.none()
