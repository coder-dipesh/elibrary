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


    path('add-to-cart/<int:book_id>', views.addToCart, name="add-to-cart"),
    path('show-cart-items', views.showCartItems, name='show-cart-items'),
    path('remove-cart-items/<int:cart_id>', views.removeCartItems, name="remove-cart-items"),
    path('order-form/<int:book_id>/<int:cart_id>', views.orderForm),


    path('my-approved-order', views.approvedOrder, name='my-approved-order'),
    path('my-pending-order', views.pendingOrder, name='my-pending-order'),
    path('my-pending-order/cancel-order/<int:order_id>', views.cancelOrder),
    path('my-returned-order', views.returnedOrder,name='my-returned-order'),


    # URLs for User-Side
    path('show-categories-user', views.showCategories, name='show-categories-user'),
    path('show-books-user', views.showBooks, name='show-books-user'),
    path('show-authors-user', views.showAuthors, name='show-authors-user'),
    path('user-all-order', views.userAllOrder, name='user-all-order'),


]
