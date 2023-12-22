from rest_framework.permissions import (
    AllowAny,
)

from npc_creator.models.feedback import Feedback


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
