from rest_framework import serializers
from task.models import Task
from blog.models import Post, Category


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'user',
            'title',
            'description',
            'complete',
        ]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'image',
            'content',
            'snippet',
            'category',
            'likes',
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
