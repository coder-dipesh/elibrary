import django_filters
from . models import Book, Author

class BookFilter(django_filters.FilterSet):
    book_name = django_filters.CharFilter(field_name='book_name', lookup_expr='icontains')
    class Meta:
        model = Book
        fields = []


class AuthorFilter(django_filters.FilterSet):
    email_contains = django_filters.CharFilter(field_name='email', lookup_expr='icontains')
    class Meta:
        model = Author
        fields = []