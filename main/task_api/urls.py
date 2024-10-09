from django.urls import path
from .views import (
    TaskApiCreateView, TaskApiListView,
    TaskApiDetailView, TaskApiUpdateView,
    PostApiCreateView, PostApiListView,
    PostApiDetailView, PostApiUpdateView,
    CategoryApiCreateView, CategoryApiDetailView,
    CategoryApiUpdateView, CategoryApiListView,
)


urlpatterns = [
    #---- Task Api Urls ----#
    path('', TaskApiListView.as_view(), name='t-list'),
    path('task/detail/<str:pk>', TaskApiDetailView.as_view(), name='t-detail'),
    path('task/create', TaskApiCreateView.as_view(), name='t-create'),
    path('task/update/<str:pk>', TaskApiUpdateView.as_view(), name='t-update'),
    #---- Post Api Urls ----#
    path('post', PostApiListView.as_view(), name='p-list'),
    path('post/detail/<str:pk>', PostApiDetailView.as_view(), name='p-detail'),
    path('post/create', PostApiCreateView.as_view(), name='p-create'),
    path('post/update/<str:pk>', PostApiUpdateView.as_view(), name='p-update'),
    #---- Category Api Urls ----#
    path('category/list', CategoryApiListView.as_view(), name='c-list'),
    path('category/create', CategoryApiCreateView.as_view(), name='c-create'),
    path('category/detail/<str:pk>', CategoryApiDetailView.as_view(), name='c-detail'),
    path('category/update/<str:pk>', CategoryApiUpdateView.as_view(), name='c-update'),
]
