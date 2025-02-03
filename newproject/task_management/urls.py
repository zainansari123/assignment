from django.urls import path, include
from .views import TaskManagement

urlpatterns = [
    path('tasks/', TaskManagement.as_view(),name='task_management'),
]
