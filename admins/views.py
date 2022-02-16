from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.auth import admin_only
from books.models import Author, Category, Order,Book
from django.contrib.auth.models import User

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

#  To send email after successfully confirming order
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage



@login_required
@admin_only
def dashboard(request):
    users = User.objects.all()
    books = Book.objects.all()
    orders = Order.objects.all()
    category = Category.objects.all()
    author = Author.objects.all()

    books_count = books.count()
    orders_count = orders.count()
    category_count = category.count()
    author_count = author.count()
    user_count = users.filter(is_staff=0).count()
    admin_count = users.filter(is_superuser=1).count()



    context={
    'totalCategories':category_count,
    'totalAuthors':author_count,
    'totalOrders':orders_count,
    'totalBooks':books_count,
    'totalUsers':user_count,
    'totalAdmins':admin_count,
    'activate_dashboard': 'active bg-dark'

    }
    return render(  request, 'admins/dashboard.html',context)


@login_required
@admin_only
def allOrders(request):
    items = Order.objects.all().order_by('-id')
    context = {
        'items': items,
        'activate_ordered_books': 'active bg-dark'
    }
    return render(request, 'admins/allOrders.html', context)

@login_required
@admin_only
def declineOrder(request, order_id):
    order = Order.objects.get(id=order_id)
    order.status = 'Declined'
    order.save()
    messages.add_message(request, messages.SUCCESS, 'Order has been declined successfully')
    return redirect('/admins/all-orders')


@login_required
@admin_only
def approveOrder(request, order_id):
    order = Order.objects.get(id=order_id)
    order.status = 'Approved'
    order.save()
    template = render_to_string('admins/orderApproved.html',{'name': request.user.username, 'book': order.book.book_name})
    email = EmailMessage(
                    'Thank you for choosing eLibrary!!',
                    template, settings.EMAIL_HOST_USER, [request.user.email],
                )
    email.fail_silently = False
    email.send()
    messages.add_message(request, messages.SUCCESS, 'Order approved and email sent successfully')
    return redirect('/admins/all-orders')


@login_required
@admin_only
def allUsers(request):
    users = User.objects.filter(is_staff=0).order_by('-id')
    context = {
        'users': users,
        'activate_users': 'active bg-dark'

    }
    return render(request, 'admins/allUsers.html', context)

@login_required
@admin_only
def allAdmins(request):
    admins = User.objects.filter(is_superuser=1).order_by('-id')
    context = {
        'admins': admins,
        'activate_admins': 'active bg-dark'

    }
    return render(request, 'admins/allAdmins.html', context)


@login_required
@admin_only
def promoteUser(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_staff = True
    user.is_superuser=True

    user.save()
    messages.add_message(request, messages.INFO, 'User promoted to Admin')
    return redirect('/admins/all-users')

@login_required
@admin_only
def deleteUser(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.add_message(request, messages.INFO, 'User removed successfully!')
    return redirect('/admins/all-users')


@login_required
@admin_only
def demoteAdmin(request, user_id):
    admin = User.objects.get(id=user_id)
    admin.is_superuser=False
    admin.is_staff = False
    admin.save()
    messages.add_message(request, messages.INFO, 'Admin demoted to user')
    return redirect('/admins/all-admins')


@login_required
@admin_only
def deactivate(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    messages.add_message(request, messages.SUCCESS, 'Admin Account Deactivated!')
    return redirect('/admins/all-admins')

@login_required
@admin_only
def reactivate(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'Admin Account Re-activated!')
    return redirect('/admins/all-admins')


@login_required
@admin_only
def adminChangePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS, "Password Changed Successfully")
            return redirect('/admins/admin-change-password')
        else:
            messages.add_message(request, messages.ERROR, "Please verify the form fields")
            return redirect('/admins/admin-change-password')

            # return redirect(request, 'admins/adminChangePassword.html', {'admin_password_change_form': form})

    context = {
        'admin_password_change_form': PasswordChangeForm(request.user),

    }
    return render(request, 'admins/adminChangePassword.html', context)