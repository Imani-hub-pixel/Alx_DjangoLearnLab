from django.db import models

# Create your models here.
class User(models.Model):
    bio=models.TextField(blank=True, null=True)
    profile_picture=models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers=models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    