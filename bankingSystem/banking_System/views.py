from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .models import NewUser
from .forms import (
    AdminAccountRegistrationForm,
    PersonalAccountRegistrationForm, 
    BusinessAccountRegistrationForm, 
    InvestorAccountRegistrationForm, 
    AdminAccountLoginForm, 
    PersonalAccountLoginForm, 
    BusinessAccountLoginForm, 
    InvestorsAccountLoginForm
)


# THE MAIN PAGE
def index_view(request):
    return render(request, 'index.html')

# GENERAL ACCOUNT REGISTRATION LOGIC
def register_account(request, form_class, template_name, login_url):
    context = {}

    # Custom view based on user type
    if request.user.is_authenticated:
        if request.user.is_personal_user():
            # Handle the request for a personal user.
            return render(request, 'personal_dashboard.html')

        elif request.user.is_business_user():
            # Handle the request for a business user.
            return render(request, 'business_dashboard.html')

        elif request.user.is_investor_user():
            # Handle the request for an investor.
            return render(request, 'investor_dashboard.html')

    # Continue with the registration logic
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(login_url)  # Redirect to the login page after registration
    else:
        form = form_class()
    context['registration_form'] = form
    return render(request, template_name, context)

# ADMIN ACCOUNT REGISTRATION
def admin_registration_view(request):
    return register_account(
        request,
        AdminAccountRegistrationForm,
        'authentication/admin/admin-reg.html',
        'admin-login'
    )

# PERSONAL ACCOUNT REGISTRATION
def personal_registration_view(request):
    return register_account(
        request,
        PersonalAccountRegistrationForm,
        'authentication/customers-reg/personal-reg.html',
        'personal-login'
    )

# BUSINESS ACCOUNT REGISTRATION
def business_registration_view(request):
    return register_account(
        request,
        BusinessAccountRegistrationForm,
        'authentication/customers-reg/business-reg.html',
        'business-login'
    )

# INVESTORS ACCOUNT REGISTRATION
def investor_registration_view(request):
    return register_account(
        request,
        InvestorAccountRegistrationForm,
        'authentication/customers-reg/investor-reg.html',
        'investor-login'
    )

# # Example of using login_required decorator
# @login_required
# def restricted_view(request):
#     return render(request, 'restricted.html')



# PERSONAL LOGIN
def personal_login_view(request):
    context = {}
    if request.method == 'POST':
        form = PersonalAccountLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Authenticating the user using email as the username
            user = authenticate(request, username=email, password=password)

            if user is not None:
                # Login the user in and redirecting to the personal dashboard
                login(request, user)
                return redirect('personal-dashboard')
            else:
                # Authentication failed, show an error message to the user
                context['error_message'] = 'Invalid email or password'

    else:
        form = PersonalAccountLoginForm()
    context['personal_login_form'] = form

    return render(request, 'authentication/customers-login/personal-login.html', context)


# BUSINESS ACCOUNT LOGIN
def business_login_view(request):
    
    return render(request, 'authentication/customers-login/business-login.html')

# INVESTORS ACCOUNT LOGIN
def investor_login_view(request):

    return render(request, 'authentication/customers-login/investor-login.html')

# ADMIN ACCOUNT LOGIN
def admin_login_view(request):

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