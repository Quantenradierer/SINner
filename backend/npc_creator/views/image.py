from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from npc_creator.models.image import Image


from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from rest_framework import serializers, viewsets


class ImageSerializer(serializers.ModelSerializer):
    file_url = serializers.ReadOnlyField()
    thumbnail_url = serializers.ReadOnlyField()

    class Meta:
        model = Image
        fields = ["id", "name", "score", "file_url", "thumbnail_url"]


class ImageViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]

    queryset = Image.objects.prefetch_related().all()
    serializer_class = ImageSerializer

    @action(detail=True, methods=["post"], permission_classes=[AllowAny])
    def upvote(self, request, pk):
        image = get_object_or_404(Image, id=pk)
        template = image.template

        image.upvote()
        image.save()
        if template:
            template.upvote()
            template.save()
        return Response({"type": "success"})

    @action(detail=True, methods=["post"], permission_classes=[AllowAny])
    def downvote(self, request, pk):
        image = get_object_or_404(Image, id=pk)
        template = image.template

        image.downvote()
        image.save()
        if template:
            template.downvote()
            template.save()
        return Response({"type": "success"})
