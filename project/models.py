from django.db import models

# Create your models here.

class cou(models.Model):
    name=models.CharField(max_length=30)
    lang=models.CharField(max_length=10)
    price=models.IntegerField()
    img=models.ImageField(upload_to='img/',null=True)
    
class re(models.Model):
    name=models.CharField(max_length=20)
    phone=models.IntegerField()
    date=models.DateTimeField()

class sign(models.Model):
    email=models.CharField(max_length=40)
    Password=models.IntegerField()