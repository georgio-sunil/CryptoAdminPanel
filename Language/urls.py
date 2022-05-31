from django.urls import path
from . import views

urlpatterns = [
    path('', views.LanguageTable.as_view(),name='language-table'),
]




