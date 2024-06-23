from rest_framework import serializers, viewsets, mixins
from rest_framework.authentication import BasicAuthentication

from npc_creator.models.collection import Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["name", "favorite"]


class CollectionViewSet(viewsets.ModelViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
