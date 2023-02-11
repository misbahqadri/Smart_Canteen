from django.db import models

# Create your models here.
class Ngos(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=70, default="")
