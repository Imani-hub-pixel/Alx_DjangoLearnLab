from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='images')
    designation=models.CharField(max_length=200)
    email_address=models.EmailField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=15,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}"