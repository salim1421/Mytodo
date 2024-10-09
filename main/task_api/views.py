from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView


from task.models import Task
from blog.models import Post, Category

from .serializer import TaskSerializer, PostSerializer, CategorySerializer


#---- Task Api View ----#
class TaskApiListView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskApiDetailView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'


class TaskApiCreateView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskApiUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'

#---- Post Api View ----#

class PostApiListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostApiCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostApiDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class PostApiUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'


#-----Category Api View ----#


class CategoryApiListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryApiCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryApiDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'


class CategoryApiUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'
