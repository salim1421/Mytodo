from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic import FormView
from django.contrib.auth import login


class RegisterPage(FormView):
    model = User
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = 'login'

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse('task-list'))
        return super().get(request, *args, **kwargs)
    

class SignInPage(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


def logout(request):
    auth.logout(request)
    return redirect('login')

