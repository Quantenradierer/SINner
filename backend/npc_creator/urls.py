from django.urls import path, include
from . import views

from django.urls import path
from rest_framework import routers

from .views import (
    EntityViewSet,
    ImageViewSet,
    FeedbackViewSet,
    FloorplanViewSet,
)

router = routers.DefaultRouter()
router.register(r"entities", EntityViewSet)
router.register(r"images", ImageViewSet)
router.register(r"feedback", FeedbackViewSet)
router.register(r"floorplans", FloorplanViewSet, basename="floorplan")

urlpatterns = [path("", include(router.urls))]
