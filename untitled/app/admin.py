from django.contrib import admin
from app.models import Board, food, Comment, Recommend

# Register your models here.
admin.site.register(Board)
admin.site.register(food)
admin.site.register(Comment)
admin.site.register(Recommend)