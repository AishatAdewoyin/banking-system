from django.shortcuts import render
from django.contrib import admin

def index_view(request):
    # View function for the home page
    return render(request, 'index.html')

def personal_registration_view(request):
    # View function for personal account registration
    return render(request, 'authentication/customers-reg/personal-reg.html')

def business_registration_view(request):
    # View function for business account registration
    return render(request, 'authentication/customers-reg/business-reg.html')

def investor_registration_view(request):
    # View function for investor account registration
    return render(request, 'authentication/customers-reg/invest-reg.html')

def personal_login_view(request):
    # View function for personal account login
    return render(request, 'authentication/customers-login/personal-login.html')

def business_login_view(request):
    # View function for business account login
    return render(request, 'authentication/customers-login/business-login.html')

def investor_login_view(request):
    # View function for investor account login
    return render(request, 'authentication/customers-login/invest-login.html')

def admin_login_view(request):
    # View function for admin account login
    return render(request, 'authentication/admin/admin-login.html')

def admin_mainpage_view(request):
    # View function for admin homepage
    return render(request, 'authentication/admin/admin-home.html')

def customers_list_view(request):
    # View function for customers list
    return render(request, 'authentication/admin/customers.html')

def single_personal_page_view(request):
    # View function for single personal customer page
    return render(request, 'authentication/admin/single-personal-customer.html')

def single_business_page_view(request):
    # View function for single business customer page
    return render(request, 'authentication/admin/single-business-customer.html')

def single_investor_page_view(request):
    # View function for single investor customer page
    return render(request, 'authentication/admin/single-investor-customer.html')

def personal_dashboard_view(request):
    # View function for personal dashboard page
    return render(request, 'authentication/customers-dashboard/personal-dashboard.html')

def business_dashboard_view(request):
    # View function for business dashboard page
    return render(request, 'authentication/customers-dashboard/business-dashboard.html')

def investor_dashboard_view(request):
    # View function for investor dashboard page
    return render(request, 'authentication/customers-dashboard/investor-dashboard.html')
