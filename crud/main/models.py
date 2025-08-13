from django.db import models

# Create your models here.
class User_Registration(models.Model):
    username=models.CharField(max_length=100,null=False,blank=False)
    password=models.CharField(max_length=10,null=False,blank=False)

class Add_Task(models.Model):
    task_name=models.CharField(max_length=100,null=False,blank=False)
    user=models.ForeignKey(User_Registration,on_delete=models.CASCADE)