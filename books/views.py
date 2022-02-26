from itertools import count
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.auth import admin_only,user_only
from books.filters import AuthorFilter, BookFilter
from books.forms import AuthorForm, BookForm, CategoryForm, OrderForm
from books.models import Author, Book, Cart, Category, Order

# For Sending Mail
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# ===================================================
# ==================== CATEGORY CRUD ================
# ===================================================

# @login_required
# @admin_only
def categoryForm(request):
    if request.method == "POST":
        form = CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category added Successfully')
            return redirect("/books/get-category")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add Category')
            return render(request, 'books/categoryForm.html', {'form_category': form})
    context = {
        'form_category': CategoryForm,
        'activate_category': 'active bg-dark',
    }
    return render(request , 'books/categoryForm.html', context)

# @login_required
# @admin_only
def getCategory(request):
    categories = Category.objects.all().order_by('-id')
    context = {
        'categories': categories,
        'activate_category': 'active bg-dark'
    }
    return render(request, 'books/getCategory.html', context)

# @login_required
# @admin_only
def deleteCategory(request,category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request, messages.SUCCESS, 'Category deleted successfully')
    return redirect('/books/get-category')

# @login_required
# @admin_only
def categoryUpdateForm(request,category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category updated Successfully')
            return redirect("/books/get-category")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update Category')
            return render(request, 'books/categoryUpdateForm.html', {'form_category': form})

    context = {
        'form_category': CategoryForm(instance=category),
        'activate_category': 'active bg-dark',
    }

    return render(request , 'books/categoryUpdateForm.html', context)

# @login_required
# @user_only
def showCategories(request):
    categories = Category.objects.all().order_by('-id')
    count= categories.count()
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    cart_count = cart_items.count()

    context = {
        'categories': categories,
        'count': count,
        'activate_category_user': 'active',
        'cart_count': cart_count,
    }
    return render(request, 'books/showCategories.html', context)

# ===================================================
# ================== CATEGORY CRUD END ==============
# ===================================================


# ===================================================
# ==================== BOOK CRUD ====================
# ===================================================

# @login_required
# @admin_only
def bookForm(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Book added Successfully')
            return redirect("/books/get-book")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add Book')
            return render(request, 'books/book_form.html', {'form_book': form})

    context = {
        'form_book': BookForm,
        'activate_books': 'active bg-dark',
    }
    return render(request, 'books/bookForm.html', context)


# @login_required
# @admin_only
def getBook(request):
    books = Book.objects.all().order_by('-id')
    book_filter = BookFilter(request.GET, queryset=books)
    books_final = book_filter.qs
    context = {
        'books': books_final,
        'activate_books': 'active bg-dark',
        'book_filter': book_filter
    }
    return render(request, 'books/getBook.html', context)

# @login_required
# @admin_only
def deleteBook(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    messages.add_message(request, messages.SUCCESS, 'Book deleted successfully')
    return redirect('/books/get-book')

# @login_required
# @admin_only
def bookUpdateForm(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Book Updated Successfully')
            return redirect("/books/get-book")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update Book')
            return render(request, 'books/book_form.html', {'form_book': form})

    context = {
        'form_book': BookForm(instance=book),
        'activate_books': 'active bg-dark',
    }
    return render(request, 'books/bookUpdateForm.html', context)

# @login_required
# @user_only
def showBooks(request):
    books = Book.objects.all().order_by('-id')
    count = books.count()
    
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    cart_count = cart_items.count()
    context = {
        'books': books,
        'count': count,
        'activate_book_user': 'active',
        'cart_count': cart_count,
    }
    return render(request, 'books/showBooks.html', context)

# ===================================================
# ================== BOOK CRUD END ==================
# ===================================================


# ===================================================
# ==================== AUTHOR CRUD ==================
# ===================================================


# @login_required
# @admin_only
def authorForm(request):
    form = AuthorForm()
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Author Added Sucessfully')
            return redirect('/books/get-author')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add author')
            return render(request, 'books/authorForm.html', {'form_author': form})

    context = {
        'form_author': AuthorForm,
        'activate_authors': 'active bg-dark'
    }
    return render(request, 'books/authorForm.html', context)


# @login_required
# @admin_only
def getAuthor(request):
    authors = Author.objects.all().order_by('-id')
    author_filter = AuthorFilter(request.GET, queryset=authors)  # to display form
    authors_final = author_filter.qs

    context = {
        'authors': authors_final,
        'activate_authors': 'active bg-dark',
        'author_filter': author_filter,
    }
    return render(request, 'books/getAuthor.html', context)


# @login_required
# @admin_only
def deleteAuthor(request, author_id):
    author = Author.objects.get(id=author_id)
    author.delete()
    messages.add_message(request, messages.SUCCESS, 'Author deleted successfully')
    return redirect('/books/get-author')

# @login_required
# @admin_only
def updateAuthor(request, author_id):
    author = Author.objects.get(id=author_id)
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect('/books/get-author')
        else:
            return render(request, 'books/authorUpdateForm.html', {'form_author': form})
    context = {
        'form_author': AuthorForm(instance=author),
        'activate_authors': 'active bg-dark',
    }
    return render(request, 'books/authorUpdateForm.html', context)


# @login_required
# @user_only
def showAuthors(request):
    authors = Author.objects.all().order_by('-id')
    count = authors.count()
    
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    cart_count = cart_items.count()
    context = {
        'authors': authors,
        'count': count,
        'activate_author': 'active',
        'cart_count': cart_count,
    }
    return render(request, 'books/showAuthors.html', context)



# ===================================================
# ================== AUTHOR CRUD END ================
# ===================================================


# ===================================================
# ================== CART & ORDER ===================
# ===================================================


# @login_required
# @user_only
def addToCart(request, book_id):
    user = request.user
    book = Book.objects.get(id=book_id)
    
    check_item_presence = Cart.objects.filter(user=user, book=book)
    
    if check_item_presence:
        messages.add_message(request, messages.ERROR, "Item is already present in cart")
        return redirect('/books/show-books-user')
    else:
        cart = Cart.objects.create(book=book, user=user)
        if cart:
            messages.add_message(request, messages.SUCCESS, 'Book added  to cart')
            return redirect('/books/show-cart-items')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add book to cart')


# @login_required
# @user_only
def showCartItems(request):
    user = request.user
    items = Cart.objects.filter(user=user)
    count= items.count()
    cart_count = items.count()


    context = {
        'items': items,
        'count': count,
        'activate_my_cart': 'active',
        'cart_count': cart_count,
    }
    return render(request, 'books/myCart.html', context)

# @login_required
# @user_only
def removeCartItems(request, cart_id):
    item = Cart.objects.get(id=cart_id)
    item.delete()
    messages.add_message(request, messages.SUCCESS, 'Cart item removed successfully')
    return redirect('/books/show-cart-items')


# @login_required
# @user_only
def orderForm(request, book_id, cart_id):
    user = request.user
    book = Book.objects.get(id=book_id)
    cart_item = Cart.objects.get(id=cart_id)
    cart_items = Cart.objects.filter(user=user)
    cart_count = cart_items.count()
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = request.POST.get('quantity')
            price = book.book_price
            total_price = int(quantity) * int(price)
            contact_no = request.POST.get('contact_no')
            contact_address = request.POST.get('contact_address')
            
            order = Order.objects.create(book=book,
                                        user=user,
                                        quantity=quantity,
                                        total_price=total_price,
                                        contact_no=contact_no,
                                        contact_address=contact_address,
                                        status="Pending"

                                        )
            if order:
                template = render_to_string('books/sendEmailTemplate.html',
                                            {'name': request.user.username, 'book': book.book_name})
                email = EmailMessage(
                    'Your order was successfully made!!',
                    template, settings.EMAIL_HOST_USER, [request.user.email],
                )
                email.fail_silently = False
                email.send()
                print("Email sent")
                messages.add_message(request, messages.SUCCESS, 'Book Ordered successfully!!!')
                cart_item.delete()
                return redirect('/books/my-pending-order')
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong')
            return render(request, 'books/orderForm.html', {'order_form': form,'cart_count':cart_count})
    context = {
        'order_form': OrderForm,
        'cart_count': cart_count,

    }
    return render(request, 'books/orderForm.html', context)


# ===================================================
# ================= END CART & ORDER ================
# ===================================================



# ===================================================
# ========= ALL, PENDING, APPROVED ORDERS ===========
# ===================================================
# @login_required
# @user_only
def userAllOrder(request):
    items = Order.objects.all().order_by('-id')
    count = items.count()
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    cart_count = cart_items.count()
    context = {
        'items': items,
        'count': count,
        'activate_myorders': 'active',
        'cart_count': cart_count,

    }
    return render(request, 'books/userAllOrder.html', context)

# @login_required
# @user_only
def approvedOrder(request):
    user = request.user
    items = Order.objects.filter(user=user, status="Approved").order_by('-id')
    count=items.count()
    cart_items = Cart.objects.filter(user=user)
    cart_count = cart_items.count()

    context = {
        'items': items,
        'count': count,
        'activate_myorders': 'active',
        'cart_count': cart_count,
    }
    return render(request, 'books/approvedOrder.html', context)

# @login_required
# @user_only
def pendingOrder(request):
    user = request.user
    items = Order.objects.filter(user=user, status="Pending").order_by('-id')
    count=items.count()
    cart_items = Cart.objects.filter(user=user)
    cart_count = cart_items.count()
    context = {
        'items': items,
        'count': count,
        'activate_myorders': 'active',
        'cart_count': cart_count,
    }
    return render(request, 'books/pendingOrder.html', context)


# @login_required
# @user_only
def cancelOrder(request, order_id):
    item = Order.objects.get(id=order_id)
    item.delete()
    messages.add_message(request, messages.SUCCESS, 'Order cancelled successfully')
    return redirect('/books/my-pending-order')


# @login_required
# @user_only
def returnedOrder(request):
    user = request.user
    items = Order.objects.filter(user=user, status="Returned").order_by('-id')
    count=items.count()
    cart_items = Cart.objects.filter(user=user)
    cart_count = cart_items.count()

    context = {
        'items': items,
        'count': count,
        'cart_count': cart_count,
        'activate_myorders': 'active',
    }
    return render(request, 'books/returnedOrder.html', context)

# ===================================================
# ========= END ALL, PENDING, APPROVED ORDERS =======
# ===================================================


