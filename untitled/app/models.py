from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    pass1 = models.CharField(max_length = 100)
    pass2 = models.CharField(max_length = 100)
    def __str__(self):
        return self.name