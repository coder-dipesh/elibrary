from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib import auth
from accounts.auth import unauthenticated_user, admin_only, user_only
from django.contrib.auth.decorators import login_required


# Create your views here.

def homepage(request):
    return render(request, 'accounts/homepage.html')

@unauthenticated_user
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            if user.is_superuser and user.is_staff and user.is_active:
                return redirect('/admins/dashboard')
            else:
                return redirect('/')
        else:
            messages.error(request, "Username or Password is incorrect.")
            return render(request, 'accounts/signin.html',{})
    context={
            'activate_login': 'active',
    }
    return render(request, 'accounts/signin.html',context)


@unauthenticated_user
def signup(request):
    if request.method=='POST':
        userdata = CreateUserForm(request.POST)
        if userdata.is_valid():
            user=userdata.save()
            user.save()
            # Profile.objects.create(user=user, username=user.username, email= user.email) 

            messages.add_message(request, messages.SUCCESS, f'{user.username} successfully registered to eLibrary.' )
            return redirect('/signin')
        else:
            context = {'form' : userdata}
            messages.add_message(request, messages.ERROR, 'Unable to register User!' )
            return render(request, 'accounts/signup.html',context)


    context ={
            'form' : CreateUserForm,
            'activate_register': 'active',
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def signout(request):
    logout(request)
    return redirect('/signin')

