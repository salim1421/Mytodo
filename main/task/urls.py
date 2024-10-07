from django.urls import path
from .views import (
    TaskListView, TaskCreateView,
    TaskDeleteView, TaskDetailView,
    TaskUpdateView,
)

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('task/create', TaskCreateView.as_view(), name='task-create'),
    path('task/detail/<str:pk>', TaskDetailView.as_view(), name='task-detail'),
    path('task/update/<str:pk>', TaskUpdateView.as_view(), name='task-update'),
    path('task/delete/<str:pk>', TaskDeleteView.as_view(), name='task-delete'),
]
