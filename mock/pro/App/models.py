from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    grade=models.CharField(max_length=10)
    image=models.ImageField()