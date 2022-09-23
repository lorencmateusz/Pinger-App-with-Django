from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from . import views

router = routers.DefaultRouter()
router.register('pinger-viewset', views.HelloViewSet, basename='pinger-viewset')
router.register('pingprofile', views.PingerProfileViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path("ip/", views.ping_ips),
    path("history/", views.view_ping_history),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

]
