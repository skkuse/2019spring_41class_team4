from django.contrib.auth import views as auth_views
from django.urls import path, include
from app.views import *
from . import views

urlpatterns = [
    path('', views.login, name='login'),
]