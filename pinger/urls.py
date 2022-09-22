from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('pinger-viewset', views.HelloViewSet, basename='pinger-viewset')
router.register('pingprofile', views.PingerProfileViewSet)

urlpatterns = [
    path("ip/", views.ping_ips),
    path("history/", views.view_ping_history),
    path('', include(router.urls))
]
