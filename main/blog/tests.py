from django.test import TestCase
from django.utils import timezone
import datetime


from .models import Post


class PostModelTest(TestCase):
    def test_was_recently_published_with_future_post(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_post = Post(date_created=time)
        self.assertIs(future_post.was_recently_published(), False)

    def test_was_recently_published_with_past_post(self):
        time = timezone.now() + datetime.timedelta(days=-30)
        past_post = Post(date_created=time)
        self.assertIs(past_post.was_recently_published(), False)

    def test_was_recently_published_with_recent_post(self):
        time = timezone.now() + datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_post = Post(date_created=time)
        self.assertIs(recent_post.was_recently_published(), False)
