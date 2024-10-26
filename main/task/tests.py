from django.test import TestCase, SimpleTestCase
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.utils import timezone
import datetime


from .models import Task
from .views import (
    TaskListView, TaskCreateView,
    TaskDeleteView, TaskDetailView,
    TaskUpdateView
)


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


class TaskUrlTest(SimpleTestCase):
    def test_task_list_url(self):
        url = reverse('task-list')
        self.assertEqual(resolve(url).func.view_class, TaskListView)

    def test_task_detail_url(self):
        url = reverse('task-detail', args=['pk'])
        self.assertEqual(resolve(url).func.view_class, TaskDetailView)

    def test_task_create_url(self):
        url = reverse('task-create')
        self.assertEqual(resolve(url).func.view_class, TaskCreateView)

    def test_task_update_url(self):
        url = reverse('task-update', args=['pk'])
        self.assertEqual(resolve(url).func.view_class, TaskUpdateView)

    def test_task_delete_url(self):
        url = reverse('task-delete', args=['pk'])
        self.assertEqual(resolve(url).func.view_class, TaskDeleteView)