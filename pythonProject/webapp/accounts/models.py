from django.db import models

# Create your models here.
class Patient(models.Model):
    full_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone_num = models.IntegerField()
    dob = models.DateTimeField(auto_now_add=True)
    house_name= models.CharField(max_length=30)
    street=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    pincode=models.IntegerField()
    password = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    medicine = models.CharField(max_length=50)
