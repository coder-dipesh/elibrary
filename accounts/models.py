from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *
from django.core import validators
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100, null=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=300, null=True)
    city = models.CharField(max_length=100,null=True)
    profile_pic = models.FileField(upload_to='static/uploads', default='static/images/user.png')
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Contact"

    def __str__(self):
        return self.name + "-" +  self.email


class Author(models.Model):
    author_name = models.CharField(max_length=200, null=True, validators=[validators.MinLengthValidator(2)])
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    email = models.EmailField(unique=True, null=True)
    profile_pic = models.FileField(upload_to='static/author_profile', null=True,
                                    default='static/user.png')
    created_date = models.DateField(auto_now_add=True, null=True)
    created_time = models.TimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.author_name