from django.urls import path, include
from . import views

urlpatterns = [
    path("ip", views.ping_ips),
]
