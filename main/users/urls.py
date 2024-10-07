from django.urls import path
from .views import RegisterPage, SignInPage, logout

urlpatterns = [
    path('register', RegisterPage.as_view(), name='register'),
    path('login', SignInPage.as_view(), name='login'),
    path('logout', logout, name='logout'),
]
