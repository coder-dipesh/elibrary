from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.auth import admin_only,user_only,unauthenticated_user
from books.filters import BookFilter
from books.forms import BookForm, CategoryForm
from books.models import Book, Category

# ===================================================
# ==================== CATEGORY CRUD ================
# ===================================================

@login_required
@admin_only
def categoryForm(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category added Successfully')
            return redirect("/books/get-category")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add Category')
            return render(request, 'books/categoryForm.html', {'form_category': form})
    context = {
        'form_category': CategoryForm,
        'activate_category': 'active',
    }
    return render(request , 'books/categoryForm.html', context)

@login_required
@admin_only
def getCategory(request):
    categories = Category.objects.all().order_by('-id')
    context = {
        'categories': categories,
        'activate_category': 'active'
    }
    return render(request, 'books/getCategory.html', context)

@login_required
@admin_only
def deleteCategory(request,category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request, messages.SUCCESS, 'Category deleted successfully')
    return redirect('/books/get-category')

@login_required
@admin_only
def categoryUpdateForm(request,category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category added Successfully')
            return redirect("/books/get-category")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update Category')
            return render(request, 'books/categoryUpdateForm.html', {'form_category': form})

    context = {
        'form_category': CategoryForm(instance=category),
        'activate_category': 'active',
    }

    return render(request , 'books/categoryForm.html', context)


# ===================================================
# ================== CATEGORY CRUD END ==============
# ===================================================


# ===================================================
# ==================== BOOK CRUD ====================
# ===================================================

@login_required
@admin_only
def bookForm(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Book added Successfully')
            return redirect("/books/get_book")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add Book')
            return render(request, 'books/book_form.html', {'form_book': form})

    context = {
        'form_book': BookForm,
        'activate_book': 'active',
    }
    return render(request, 'books/bookForm.html', context)


@login_required
@admin_only
def getBook(request):
    books = Book.objects.all().order_by('-id')
    book_filter = BookFilter(request.GET, queryset=books)
    books_final = book_filter.qs
    context = {
        'books': books_final,
        'activate_book': 'active',
        'book_filter': book_filter
    }
    return render(request, 'books/getBook.html', context)

@login_required
@admin_only
def deleteBook(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    messages.add_message(request, messages.SUCCESS, 'Book deleted successfully')
    return redirect('books/get-book')

@login_required
@admin_only
def bookUpdateForm(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Book Updated Successfully')
            return redirect("/books/get_book")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update Book')
            return render(request, 'books/book_form.html', {'form_book': form})

    context = {
        'form_book': BookForm(instance=book),
        'activate_book': 'active',
    }
    return render(request, 'books/bookUpdateForm.html', context)
