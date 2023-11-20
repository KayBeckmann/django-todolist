from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Todo(models.Model):
  title = models.CharField(max_length=30)
  description = models.CharField(max_length=30)
  created_at = models.DateField(default=datetime.date.today)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self): #Overview in adminpanel
    return f"{self.created_at}: {self.user} -> {self.title} "