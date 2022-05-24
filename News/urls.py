from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.NewsTable.as_view(),name='news'),
    path('/create', views.CreateNews.as_view(), name='news-create'),
    path('/update/<str:pk>', views.UpdateNews.as_view(), name='news-update'),

    path('/news-feed', views.NewsFeedTable.as_view(), name='news-feed')
]