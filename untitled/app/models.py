from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=30, blank=True)
    created_date = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=500, blank=True)
    view = models.IntegerField(blank=True)

class food(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50,null=True)
    body = models.TextField(max_length=1024,null=True)
    date = models.DateTimeField(auto_created=True,auto_now_add=True,null=True)
    price = models.IntegerField(default=0)

    def generate(self):
        self.food =""
        self.save() #db에저장

    def __str__(self):
        return self.name