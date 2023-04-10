from django.urls import path, include

from . import views

from django.urls import path
from rest_framework import routers, serializers, viewsets

from npc_creator.models import Npc


# Serializers define the API representation.
class NpcSerializer(serializers.ModelSerializer):
    attributes = serializers.DictField()
    class Meta:
        model = Npc
        fields = [field.name for field in Npc._meta.fields] + ['attributes']


class UserViewSet(viewsets.ModelViewSet):
    queryset = Npc.objects.order_by('-id').prefetch_related().all()
    serializer_class = NpcSerializer

    def get_queryset(self):
        search_text = self.request.query_params.get('search', '')
        moderated = self.request.query_params.get('moderated', '') == 'on'

        states = [Npc.State.MODERATED]
        if not moderated:
            states.append(Npc.State.CREATED)

        return self.queryset.filter(attribute__value__icontains=search_text, state__in=states).distinct()


router = routers.DefaultRouter()
router.register(r'npcs', UserViewSet)

urlpatterns = [
    path('npcs/random/', views.random_npc, name='get a random npc'),
    path('npcs/prompt', views.npc, name='create npc'),
    path('npcs/prev', views.prev_npc, name='get the prev npc'),
    path('npcs/next', views.next_npc, name='get the next npc'),
    path('', include(router.urls)),
]
