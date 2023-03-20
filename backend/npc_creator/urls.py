from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('npc/<int:id>', views.read_npc, name='npc'),
    path('npc', views.npc, name='npc')
]
