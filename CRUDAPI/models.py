from django.db import models
from djongo import models
# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='images')
    summery= models.TextField()