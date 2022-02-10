from django.db import models
from django.core.validators import *
from django.core import validators
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=200, null=True, validators=[validators.MinLengthValidator(2)])
    category_image = models.ImageField(upload_to='static/category', null=True)
    category_description = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.category_name


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200, null=True)
    book_price = models.FloatField()
    stock = models.IntegerField(null=True)
    book_image = models.ImageField(upload_to='static/uploads')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, )
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.book_name




class Author(models.Model):
    author_name = models.CharField(max_length=200, null=True, validators=[validators.MinLengthValidator(2)])
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    email = models.EmailField(unique=True, null=True)
    profile_pic = models.FileField(upload_to='static/author_profile', null=True,
                                    default='static/user.png')
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.author_name