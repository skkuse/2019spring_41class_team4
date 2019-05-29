"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from app.views import *
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.main, name='main'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('community/', views.community, name='community'),
    path('community/<int:board_id>', views.view_post, name='community_view'),
    path('community/write', views.write_post, name='community_write'),
    path('community/submit', views.submit_post, name='community_submit'),
    path('purchase/', views.purchase, name='purchase'),
    path('foodreg/', views.foodreg, name='foodreg'),
    path('foodreg/submit', views.submit_food, name='food_submit'),
    path('', views.login, name='login'),
]
