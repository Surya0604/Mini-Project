from django.db import models
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    pdf=models.FileField(upload_to='book/pdf')
    cover=models.ImageField(upload_to='book/cover',null=True,blank=True)
# Create your models here.
