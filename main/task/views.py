from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Task


class TaskListView(ListView):
    model = Task


class TaskDetaillView(DetailView):
    model = Task


class TaskCreateView(CreateView):
    model = Task


class TaskUpdateView(UpdateView):
    model = Task


class TaskDeleteView(DeleteView):
    model = Task
    success_url = 'task-list'
