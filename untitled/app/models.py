from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=30, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    view = models.IntegerField(default=0)

class food(models.Model):
    name = models.CharField(max_length=50)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='foods')
    body = models.CharField(max_length=1024)
    photo = models.ImageField(blank=True)
    date = models.DateTimeField(auto_created=True, auto_now_add=True)
    price = models.IntegerField(default=0)
    view = models.IntegerField(default=0)
    category = models.CharField(max_length=20, default=0)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)

    def generate(self):
        self.food =""
        self.save() #db에저장

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='comments')
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_contents = models.CharField(max_length=200)
    comment_writer = models.CharField(max_length=30, blank=True)

    class Meta:
        ordering = ['-id']

class Recommend(models.Model):
    viewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recommendation')
    view = models.IntegerField(default=0)
    item = models.CharField(max_length=50)

class Location(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)