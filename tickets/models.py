from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class newticket(models.Model):
    Department = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    subject = models.CharField(max_length=40)
    Description = models.CharField(max_length=400)
    Contact_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    priority = models.CharField(max_length=40)
    file = models.FileField(upload_to='media')
    uid = User.id