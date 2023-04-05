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

        return self.queryset.filter(attribute__value__contains=search_text, state__in=states).distinct()


router = routers.DefaultRouter()
router.register(r'npcs', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('npc/random', views.random_npc, name='get a random npc'),
    path('npc/prev', views.prev_npc, name='get the prev npc'),
    path('npc/next', views.next_npc, name='get the next npc'),
    path('npc/<int:id>', views.read_npc, name='npc'),
    path('npc', views.npc, name='npc')
]
