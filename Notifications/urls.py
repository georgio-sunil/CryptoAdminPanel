from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', views.PushNotifications.as_view(),name='notifications'),
    path('api/getNotifications', views.getNotifications),
]