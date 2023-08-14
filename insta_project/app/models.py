from django.db import models

# Create your models here.

class post(models.Model):
    userName = models.CharField(max_length=20)
    posts = models.TextField()



def __str__(self):
    return f"{self.userName}:{self.content}"