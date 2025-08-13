from django.db import models
from django.utils import timezone
# Create your models here.


class User_Registration(models.Model):
    username = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=10, null=False, blank=False)


class Add_Task(models.Model):
    task_name = models.CharField(max_length=500, null=False, blank=False)
    user = models.ForeignKey(User_Registration, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    task_done = models.IntegerField(default=False)
