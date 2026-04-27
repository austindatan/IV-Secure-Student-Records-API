from django.contrib.auth.models import User
from django.db import models

class StudentRecord(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    course = models.CharField(max_length=50)
    year_level = models.IntegerField()
