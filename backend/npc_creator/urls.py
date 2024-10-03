from django.urls import path, include
from . import views

from django.urls import path
from rest_framework import routers

from .views import (
    EntityViewSet,
    ImageViewSet,
    FeedbackViewSet,
)

router = routers.DefaultRouter()
router.register(r"entities", EntityViewSet)
router.register(r"images", ImageViewSet)
router.register(r"feedback", FeedbackViewSet)

urlpatterns = [path("", include(router.urls))]
