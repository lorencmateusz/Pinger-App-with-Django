from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from . import views

router = routers.DefaultRouter()
router.register('pinger-app', views.PingerViewSet, basename='pinger-app')
router.register('pinger-manual-add', views.HelloViewSet, basename='pinger-manual-add')
router.register('ping-history', views.PingerProfileViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path("history/", views.view_ping_history),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

]
