from django.urls import path
from . import views

urlpatterns = [
    
    # Course Routing    
    path('', views.CourseTable.as_view(), name='courses'),
    path('details/<str:pk>', views.ViewCourse.as_view(), name='course-details'),

    # Topics Routing
    path('details/<str:pk>/topics/add', views.AddTopic.as_view(), name='topic-add'),
    path('details/<str:pk>/topics/details', views.UpdateTopic.as_view(), name='topic-detail'),

    # Category Routing
    path('categories', views.CategoriesTable.as_view(), name='categories-list'),
]