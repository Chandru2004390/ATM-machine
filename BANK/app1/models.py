from django.db import models

# Create your models here.


class Users(models.Model):
    First_Name=models.CharField(max_length=30)
    Last_Name=models.CharField(max_length=30)
    Password=models.CharField(max_length=10)
    Pin=models.CharField(max_length=4)
    Mobile_Number=models.CharField(max_length=12)
    Acc_No=models.CharField(max_length=11,unique=True)
    Balance=models.IntegerField()
