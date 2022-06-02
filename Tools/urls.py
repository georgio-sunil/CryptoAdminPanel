from django.urls import path
from . import views

urlpatterns = [
    path('', views.BannerTable.as_view(),name='banner-table'),
]


