from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.CoinTable.as_view(),name='coin-tables'),
]




