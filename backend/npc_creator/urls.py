from django.urls import path

from . import views

urlpatterns = [
    path('npc/random', views.random_npc, name='get a random npc'),
    path('npc/prev', views.prev_npc, name='get the prev npc'),
    path('npc/next', views.next_npc, name='get the next npc'),
    path('npc/<int:id>', views.read_npc, name='npc'),
    path('npc', views.npc, name='npc')
]
