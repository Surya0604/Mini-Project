from django.db import models
class book(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=25)
    img=models.CharField(max_length=300)
# Create your models here.
