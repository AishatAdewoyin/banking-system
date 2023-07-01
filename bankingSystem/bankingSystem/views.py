from django.shortcuts import render
from django.contrib import admin

#first page's requests
def index_view(request):
    # View function for the home page
    return render(request, 'index.html')

def personal_registration_view(request):
    # View function for personal account registration
    return render(request, 'customers-reg/personal-reg.html')

def business_registration_view(request):
    # View function for business account registration
    return render(request, 'customers-reg/business-reg.html')

def investor_registration_view(request):
    # View function for investor account registration
    return render(request, 'customers-reg/invest-reg.html')

def personal_login_view(request):
    # View function for personal account login
    return render(request, 'customers-login/personal-login.html')

def business_login_view(request):
    # View function for business account login
    return render(request, 'customers-login/business-login.html')

def investor_login_view(request):
    # View function for investor account login
    return render(request, 'customers-login/invest-login.html')

def admin_login_view(request):
    # View function for admin account login
    return render(request, 'admin/admin-login.html')


