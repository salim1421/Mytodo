from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone


from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    paginate_by = 5
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(date_created__lte=timezone.now()).order_by('-date_created')
    
    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area')
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
        context["search_input"] = search_input
        return context
    


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task

    def get_queryset(self):
        return Task.objects.filter(date_created__lte=timezone.now())


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = [
        'title',
        'description',
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = [
        'title',
        'description',
        'complete'
    ]
    success_url = '/'


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = '/'
    