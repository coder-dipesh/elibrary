from django.shortcuts import render
from accounts.auth import admin_only
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
@admin_only
def dashboard(request):
  return render(  request, 'admins/dashboard.html')