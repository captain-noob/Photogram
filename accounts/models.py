from django.db import models

# Create your models here.
class user_detials(models.Model):
    username=models.CharField(max_length=20)
    name=models.CharField(max_length=52)
    phonenumber=models.IntegerField()
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=20)
    propic=models.CharField(max_length=100)
    post=models.IntegerField(default=0)
    followings=models.IntegerField()
    followers=models.IntegerField()
    verified=models.IntegerField(default=0)
    date=models.DateField()
    report=models.IntegerField(default=0)

