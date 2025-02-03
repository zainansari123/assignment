from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Task(models.Model):
    task_id= models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=100)
    task_descriptioon=models.TextField(blank=True,default='')
    created_by= models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    created_on= models.DateTimeField(auto_created=True,default=datetime.now())

    def __str__(self):
        return str(self.task_id)

