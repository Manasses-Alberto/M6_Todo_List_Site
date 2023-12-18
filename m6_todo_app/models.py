from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
    ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    start = models.CharField(max_length=18)
    end = models.CharField(max_length=18)
    description = models.TextField(null=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
