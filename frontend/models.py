
from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Category'



class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to="document")
    price = models.IntegerField()
    created_by = models.CharField(max_length=50)
    description = models.TextField()
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    def total_likes(self):
        return self.likes.count()

    class Meta():
        verbose_name_plural = 'Product'





class Profile(models.Model):
    name = models.CharField(max_length=150)
    upload = models.FileField(upload_to='profile_upload')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Profile'



class NewsLetter(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'NewsLetter'

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=700)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'NewsLetter'







