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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.main, name='main'),
    path('main/food=<int:food_id>', views.view_food1, name='food_view1'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('community/', views.community, name='community'),
    path('community/post=<int:board_id>', views.view_post, name='community_view'),
    path('community/write', views.write_post, name='community_write'),
    path('community/submit', views.submit_post, name='community_submit'),
    path('community/post=<int:board_id>/comment_write', views.comment_write, name='comment_write'),
    path('purchase/', views.purchase, name='purchase'),
    path('foodreg/', views.foodreg, name='foodreg'),
    path('foodreg/submit', views.submit_food, name='food_submit'),
    path('', views.login, name='login'),
    path('foodlist/', views.foodlist, name='foodlist'),
    path('foodlist/food=<int:food_id>', views.view_food, name='food_view'),
    path('foodlist/food=<int:food_id>/purchase', views.purchase, name='food_purchase'),
    path('foodlist/search', views.search1, name='search1'),
    path('foodlist/search=<str:word>/', views.search_food, name='search_food'),
    path('community/search', views.search2, name='search2'),
    path('community/search=<str:word>/', views.search_post, name='search_post'),
    path('main/get_location/', views.get_latlng, name='get_latlng'),
    path('myfoodlist/', views.myfood, name='my_food'),
    path('myfoodlist/food=<int:food_id>/chat', views.myfood_chat, name='my_food_chat'),
    path('foodlist/cooked',views.cooked,name='cooked'),
    path('foodlist/meat', views.meat, name='meat'),
    path('foodlist/vegetable', views.vegetable, name='vegetable'),
    path('foodlist/cooked', views.fish, name='fish'),
    path('foodlist/category=<str:word>/', views.category, name='category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
