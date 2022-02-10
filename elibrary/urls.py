

from django.urls import include, path

urlpatterns = [
    path('', include('accounts.urls')),
    path('admins/', include('admins.urls')),
    path('books/', include('books.urls')),
]
