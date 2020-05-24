from django.db import models
from accounts.models import user_detials
# Create your models here.
class imguploads(models.Model):
    cusid=models.ForeignKey(user_detials,on_delete=models.CASCADE)
    image=models.CharField(max_length=100,unique=True)
    caption=models.CharField(max_length=70)
    likes=models.IntegerField()
    command=models.IntegerField()
    report=models.IntegerField(default=0)


