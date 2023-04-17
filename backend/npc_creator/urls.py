from django.urls import path, include
from . import views

from django.urls import path
from rest_framework import routers, serializers, viewsets

from .views import NpcViewSet

router = routers.DefaultRouter()
router.register(r'npcs', NpcViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
