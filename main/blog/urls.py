from django.urls import path
from .views import PostDetailView, CategoryView


urlpatterns = [
    path('post/<str:pk>', PostDetailView.as_view(), name='post-detail'),
    path('posts/<category>', CategoryView.as_view(), name='category'),
]
