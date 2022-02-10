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

    path('author-form', views.authorForm, name='author-form'),
    path('get-author', views.getAuthor, name='get-author'),
    path('delete-author/<int:author_id>', views.deleteAuthor, name='delete-author'),
    path('update-author/<int:author_id>', views.updateAuthor, name='update-author'),

    # URLs for User-Side
    path('show-categories-user', views.showCategories, name='show-categories-user'),
    path('show-books-user', views.showBooks, name='show-books-user'),
    path('show-authors-user', views.showAuthors, name='show-authors-user'),

]
