from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginPage, name="new_login"),
    path('login/', views.loginPage, name='login'),
    path('dashboard/', views.dashboard, name="dashboard"),

    path('vertical-boxed', views.Boxed.as_view(),name='vertical-boxed'),
    path('vertical-light-sidebar', views.Lightsidebar.as_view(),name='vertical-light-sidebar'),
    path('vertical-compact-sidebar', views.CompactSidebar.as_view(),name='vertical-compact-sidebar'),
    path('vertical-icon-sidebar', views.IconSidebar.as_view(),name='vertical-icon-sidebar'),

    path('coin', include('Coins.urls')),
    path('news/', include('News.urls')),
    path('courses/', include('Academy.urls')),
    path('language/', include('Language.urls'))
]
