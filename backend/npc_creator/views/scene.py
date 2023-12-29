from rest_framework.authentication import TokenAuthentication

from rest_framework import serializers, viewsets

from npc_creator.models import Scene


class SceneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scene
        fields = ["title", "entities"]


class SceneViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    serializer_class = SceneSerializer
    queryset = Scene.objects.none()

    def get_queryset(self):
        return Scene.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)