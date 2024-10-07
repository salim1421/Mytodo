from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
import datetime


class Category(models.Model):
    category_name = models.CharField(max_length=299)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=299)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    content = models.TextField()
    snippet = models.CharField(max_length=299)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_post')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
    def was_recently_published(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_created <= now

