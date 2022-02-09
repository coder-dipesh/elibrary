from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.auth import admin_only,user_only,unauthenticated_user
# Create your views here.


def dashboard(request):
  return render(  request, 'admins/dashboard.html')