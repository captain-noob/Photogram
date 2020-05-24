from django.db import models
from accounts.models import user_detials
# Create your models here.

class followers(models.Model):
    myuname=models.CharField(max_length=20)
    myid=models.ForeignKey(user_detials,on_delete=models.CASCADE,related_name='+')
    foll_uname=models.CharField(max_length=30)
    foll_uid=models.ForeignKey(user_detials,on_delete=models.CASCADE,related_name='+')

class followings(models.Model):
    myusname=models.CharField(max_length=20)
    myuid=models.ForeignKey(user_detials,on_delete=models.CASCADE,related_name='+')
    follw_uname=models.CharField(max_length=30)
    follw_uid=models.ForeignKey(user_detials,on_delete=models.CASCADE,related_name='+')