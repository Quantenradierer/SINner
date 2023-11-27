from django.urls import path, include
from . import views

from django.urls import path
from rest_framework import routers

from .views import NpcViewSet, LocationViewSet, CustomViewSet, ImageViewSet

router = routers.DefaultRouter()
router.register(r"npcs", NpcViewSet)
router.register(r"locations", LocationViewSet)
router.register(r"customs", CustomViewSet)
router.register(r"images", ImageViewSet)

urlpatterns = [path("", include(router.urls))]
