from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime

# Create your models here.
class post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=70)
    content=models.CharField(max_length=350)
    date =models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.title