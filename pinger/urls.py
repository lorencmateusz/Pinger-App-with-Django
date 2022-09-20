from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter

urlpatterns = [
    path("ip/", views.ping_ips),
    path("history/", views.view_ping_history),
]
