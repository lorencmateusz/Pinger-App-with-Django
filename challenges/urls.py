from django.urls import path, include
from . import views

urlpatterns = [
    path("january", views.index),
    path('february', views.index),
    path('<month>', views.monthly_challenges)
]
