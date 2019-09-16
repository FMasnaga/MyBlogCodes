from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vr.api.views import ProfileViewSet

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)

urlpatterns = [
    path("", include(router.urls))
]