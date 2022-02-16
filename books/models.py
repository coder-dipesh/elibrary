from django.db import models
from django.core.validators import *
from django.core import validators
from django.contrib.auth.models import User
from accounts.models import Author

class Category(models.Model):
    category_name = models.CharField(max_length=200, null=True, validators=[validators.MinLengthValidator(2)])
    category_image = models.ImageField(upload_to='static/category', null=True)
    category_description = models.TextField(null=True)
    created_date = models.DateField(auto_now_add=True, null=True)
    

    def __str__(self):
        return self.category_name


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    # book_author = models.CharField(max_length=200, null=True)
    book_price = models.FloatField()
    stock = models.IntegerField(null=True)
    book_image = models.ImageField(upload_to='static/uploads')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, )
    created_date = models.DateField(auto_now_add=True, null=True)
    created_time = models.TimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.book_name



# class Author(models.Model):
#     author_name = models.CharField(max_length=200, null=True, validators=[validators.MinLengthValidator(2)])
#     firstname = models.CharField(max_length=50, null=True)
#     lastname = models.CharField(max_length=50, null=True)
#     email = models.EmailField(unique=True, null=True)
#     profile_pic = models.FileField(upload_to='static/author_profile', null=True,
#                                     default='static/user.png')
#     created_date = models.DateField(auto_now_add=True, null=True)
#     created_time = models.TimeField(auto_now_add=True, null=True)


#     def __str__(self):
#         return self.author_name

class Cart(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True, null=True)


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    )
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    total_price = models.IntegerField(null=True)
    status = models.CharField(max_length=200, choices=STATUS, null=True)
    contact_no = models.CharField(validators=[MinLengthValidator(9), MaxLengthValidator(10)], null=True, max_length=10)
    contact_address = models.CharField(max_length=200, null=True)
    created_date = models.DateField(auto_now_add=True, null=True)
    created_time = models.TimeField(auto_now_add=True, null=True)
