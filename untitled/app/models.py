from django.db import models

# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=30, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500, blank=True)
    view = models.IntegerField(default=0)

class food(models.Model):
    name = models.CharField(max_length=50)
    seller = models.CharField(max_length=30, blank=True)
    body = models.CharField(max_length=1024)
    date = models.DateTimeField(auto_created=True, auto_now_add=True)
    price = models.IntegerField(default=0)

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