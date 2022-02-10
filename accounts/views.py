from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateUserForm, ProfileForm
from django.contrib import auth
from accounts.auth import unauthenticated_user, admin_only, user_only
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
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
            Profile.objects.create(user=user, username=user.username, email= user.email) 

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



@login_required
@user_only
def getProfile(request):
    profile = request.user.profile
    context = {
        'profile': profile,
        'activate_profile': 'active'
    }
    return render(request, 'accounts/userProfile.html', context)


@login_required
@user_only
def updateUserProfile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Profile updated successfully")
            return redirect('/user-profile')
    context = {
        'profile': profile,
        'profileUpdateForm': ProfileForm(instance=profile),
        'activate_profile': 'active'
    }
    return render(request, 'accounts/updateUserProfile.html', context)



@login_required
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS, "Password Changed Successfully")
            return redirect('/change-password')
        else:
            messages.add_message(request, messages.ERROR, "Please verify the form fields")
            return redirect(request, 'accounts/changePassword.html', {'password_change_form': form})

    context = {
        'password_change_form': PasswordChangeForm(request.user),

    }
    return render(request, 'accounts/changePassword.html', context)
