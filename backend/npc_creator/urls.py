from django.urls import path, include
from . import views

from django.urls import path
from rest_framework import routers

from .views import NpcViewSet, ImageViewSet

router = routers.DefaultRouter()
router.register(r"npcs", NpcViewSet)
router.register(r"images", ImageViewSet)

urlpatterns = [
    path("", include(router.urls))
]
