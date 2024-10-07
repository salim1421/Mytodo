from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
import datetime


from .models import Task


class TaskModelTest(TestCase):
    def test_was_created_recently_with_past_task(self):
        time = timezone.now() + datetime.timedelta(days=-30)
        past_task = Task(date_created=time)
        self.assertIs(past_task.was_recently_created(), False)

    def test_was_created_recently_with_future_task(self):
        time = timezone.now() + datetime.timedelta(days=1, seconds=1)
        future_task = Task(date_created=time)
        self.assertIs(future_task.was_recently_created(), False)

    def test_was_created_recently_with_recent_task(self):
        time = timezone.now() + datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_task = Task(date_created=time)
        self.assertIs(recent_task.was_recently_created(), False)


