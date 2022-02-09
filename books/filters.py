import django_filters
from . models import Author, Book, User, Order

class BookFilter(django_filters.FilterSet):
    book_name = django_filters.CharFilter(field_name='book_name', lookup_expr='icontains')
    class Meta:
        model = Book
        fields = []
