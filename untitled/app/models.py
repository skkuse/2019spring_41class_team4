from django.db import models

# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=30, blank=True)
    created_date = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=500, blank=True)
    view = models.IntegerField(blank=True)

class food(models.Model):
    name = models.CharField(max_length=50)
    body = models.CharField(max_length=1024)
    date = models.DateTimeField(auto_created=True,auto_now_add=True)

    def generate(self):
        self.food =""
        self.save() #db에저장

    def __str__(self):
        return self.name