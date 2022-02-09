from django.urls import  path
from . import views

urlpatterns = [
    path('category-form', views.categoryForm, name='category-form'),
    path('get-category', views.getCategory, name='get-category'),
    path('delete-category/<int:category_id>', views.deleteCategory, name='delete-category'),
    path('update-category/<int:category_id>', views.categoryUpdateForm, name='update_category'),

    path('book-form', views.bookForm, name='book-form'),
    path('get-book', views.getBook, name='get-book'),
    path('delete-book/<int:book_id>', views.deleteBook, name='delete-book'),
    path('update-book/<int:book_id>', views.bookUpdateForm, name='update-book'),
]
