from django.forms import ModelForm

from .models import Category, Book, Author, Order


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['quantity', 'contact_no', 'contact_address']
