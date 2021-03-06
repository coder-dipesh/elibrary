import django_filters
from . models import Book, Author, Order

class BookFilter(django_filters.FilterSet):
    book_name = django_filters.CharFilter(field_name='book_name')
    class Meta:
        model = Book
        fields = []


class AuthorFilter(django_filters.FilterSet):
    email_contains = django_filters.CharFilter(field_name='email')
    class Meta:
        model = Author
        fields = []


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = '__all__'
















