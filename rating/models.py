from django.db import models
from accounts.models import user_detials
from upload.models import imguploads
# Create your models here.

class likes(models.Model):
    cus_id=models.ForeignKey(user_detials,on_delete=models.CASCADE,related_name="+")
    photo_id=models.ForeignKey(imguploads,on_delete=models.CASCADE,related_name="+")

class comments(models.Model):
    cus_id = models.ForeignKey(user_detials, on_delete=models.CASCADE,related_name="+")
    photo_id = models.ForeignKey(imguploads, on_delete=models.CASCADE,related_name="+")
    comments=models.CharField(max_length=1000)