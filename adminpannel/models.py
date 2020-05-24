from django.db import models

# Create your models here.
class admin(models.Model):
    username=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=30,unique=True)
    phone=models.BigIntegerField(unique=True)
    name=models.CharField(max_length=30)