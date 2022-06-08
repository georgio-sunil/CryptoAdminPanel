from django.urls import path
from . import views

urlpatterns = [
    path('banner', views.BannerTable.as_view(),name='banner-table'),
    path('banner/<str:pk>', views.UpdateBannerDetails.as_view(), name='update-banner'),
    path('faq', views.FAQTable.as_view(), name='faq'),
    path('faq/<str:pk>', views.UpdateFAQDetails.as_view(), name='update-faq')
]