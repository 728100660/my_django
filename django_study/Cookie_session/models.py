from django.db import models

# Create your models here.
class students(models.Model):
    username = models.CharField(max_length=6)
    password = models.CharField(max_length=20)
    token = models.CharField(max_length=40,default=None)