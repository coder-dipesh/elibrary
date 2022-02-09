from django import forms
from django.forms import ModelForm

from .models import Category, Book


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
