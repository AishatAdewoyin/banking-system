from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .models import User
from .forms import AdminAccountRegistrationForm, PersonalAccountRegistrationForm, BusinessAccountRegistrationForm, InvestorAccountRegistrationForm


# THE MAIN PAGE
def index_view(request):
    return render(request, 'index.html')

# ADMIN ACCOUNT REGISTRATION
def admin_registration_view(request):
    context={}
    if request.method == 'POST':
        form = AdminAccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-login')  # Redirect to admin login after registration
        context['admin_registration']=form
    else:
        form = AdminAccountRegistrationForm()
        context['admin_registration']=form

    return render(request, 'authentication/customers-reg/admin-reg.html', context)

# PERSONAL ACCOUNT REGISTRATION
def personal_registration_view(request):
    context={}
    if request.method == 'POST':
        form = PersonalAccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personal-login')  # Redirect to personal login after registration
        context['personal_account_registration']=form
    else:
        form = PersonalAccountRegistrationForm()
        context['personal_account_registration']=form
       
    return render(request, 'authentication/customers-reg/personal-reg.html', context)

# BUSINESS ACCOUNT REGISTRATION
def business_registration_view(request):
    context={}
    if request.method == 'POST':
        form = BusinessAccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('business-login')  # Redirect to personal login after registration
        context['business_account_registration']=form
    else:
        form = BusinessAccountRegistrationForm()
        context['business_account_registration']=form

    return render(request, 'authentication/customers-reg/business-reg.html', context)


# INVESTORS ACCOUNT REGISTRATION
def investor_registration_view(request):
    context={}
    if request.method == 'POST':
        form = InvestorAccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('investor-login')  # Redirect to investor login after registration
        context['investors_account_registration']=form
    else:
        form = InvestorAccountRegistrationForm()
        context['investors_account_registration']=form

    return render(request, 'authentication/customers-reg/investor-reg.html', context)

# PERSONAL LOGIN
def personal_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user and user.role == User.Role.PERSONAL_ACCOUNTS:
            login(request, user)
            return redirect('personal-dashboard')
        else:
            error_message = "Invalid credentials or unauthorized role."
            return render(request, 'authentication/customers-login/personal-login.html', {'error_message': error_message})

    return render(request, 'authentication/customers-login/personal-login.html')

# BUSINESS ACCOUNT LOGIN
def business_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user and user.role == User.Role.BUSINESS_ACCOUNTS:
            login(request, user)
            return redirect('business-dashboard')
        else:
            error_message = "Invalid credentials or unauthorized role."
            return render(request, 'authentication/customers-login/business-login.html', {'error_message': error_message})

    return render(request, 'authentication/customers-login/business-login.html')

# INVESTORS ACCOUNT LOGIN
def investor_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user and user.role == User.Role.BUSINESS_ACCOUNTS:
            login(request, user)
            return redirect('investor-dashboard')
        else:
            error_message = "Invalid credentials or unauthorized role."
            return render(request, 'authentication/customers-login/investor-login.html', {'error_message': error_message})

    return render(request, 'authentication/customers-login/investor-login.html')

# ADMIN ACCOUNT LOGIN
def admin_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user and user.role == User.Role.ADMIN:
            login(request, user)
            return redirect('admin-mainpage')
        else:
            error_message = "Invalid credentials or unauthorized role."
            return render(request, 'authentication/admin/admin-login.html', {'error_message': error_message})

    return render(request, 'authentication/admin/admin-login.html')


def admin_mainpage_view(request):
    # View function for admin homepage
    return render(request, 'authentication/admin/admin-mainpage.html')

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


@login_required
def personal_password_reset_view(request):
    # View function for password reset page
    return render(request, 'authentication/customers-reset-password/personal-password-reset.html')


def business_password_reset_view(request):
    # View function for business password reset page
    return render(request, 'authentication/customers-reset-password/business-password-reset.html')


def investors_password_reset_view(request):
    # View function for investors password reset page
    return render(request, 'authentication/customers-reset-password/investors-password-reset.html')