from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import PersonalAccount, BusinessAccount, InvestorAccount

# THE MAIN PAGE
def index_view(request):
    return render(request, 'index.html')

# AUTHENTICATION

# PERSONAL ACCOUNT REGISTRATION
def personal_registration_view(request):
    if request.method == 'POST':
        fullname = request.POST.get('fname')
        email = request.POST.get('email')
        user_password = request.POST.get('password')
        user_address = request.POST.get('address')
        user_address2 = request.POST.get('address2')
        user_city = request.POST.get('city')
        user_state = request.POST.get('state')
        user_zipcode = request.POST.get('zipcode')

        # Hashing the password
        hashed_password = make_password(user_password)

        new_personal = PersonalAccount.objects.create_user(
            username=email,
            email=email,
            password=hashed_password,
            fullname=fullname,
            user_address=user_address,
            user_address2=user_address2,
            user_city=user_city,
            user_state=user_state,
            user_zipcode=user_zipcode
        )

        return redirect('personal-login')

    return render(request, 'authentication/customers-reg/personal-reg.html')

# BUSINESS ACCOUNT REGISTRATION
def business_registration_view(request):
    if request.method == 'POST':
        fullname = request.POST.get('fname')
        email = request.POST.get('email')
        user_password = request.POST.get('password')
        user_address = request.POST.get('address')
        user_address2 = request.POST.get('address2')
        user_city = request.POST.get('city')
        user_state = request.POST.get('state')
        user_zipcode = request.POST.get('zipcode')

        # Hashing the password
        hashed_password = make_password(user_password)

        new_business = BusinessAccount.objects.create_user(
            username=email,
            email=email,
            password=hashed_password,
            fullname=fullname,
            user_address=user_address,
            user_address2=user_address2,
            user_city=user_city,
            user_state=user_state,
            user_zipcode=user_zipcode
        )

        return redirect('business-login')

    return render(request, 'authentication/customers-reg/business-reg.html')

# INVESTORS ACCOUNT REGISTRATION
def investor_registration_view(request):
    if request.method == 'POST':
        fullname = request.POST.get('fname')
        email = request.POST.get('email')
        user_password = request.POST.get('password')
        user_address = request.POST.get('address')
        user_address2 = request.POST.get('address2')
        user_city = request.POST.get('city')
        user_state = request.POST.get('state')
        user_zipcode = request.POST.get('zipcode')

        # Hashing the password
        hashed_password = make_password(user_password)

        new_investor = InvestorAccount.objects.create_user(
            username=email,
            email=email,
            password=hashed_password,
            fullname=fullname,
            user_address=user_address,
            user_address2=user_address2,
            user_city=user_city,
            user_state=user_state,
            user_zipcode=user_zipcode
        )

        return redirect('investor-login')

    return render(request, 'authentication/customers-reg/invest-reg.html')

# ...

# PERSONAL ACCOUNT LOGIN
def personal_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticating the user
        user = authenticate(request, username=email, password=password)

        if user and user.role == UserModel.Role.PERSONAL_ACCOUNTS:
            # Logging the user in if authentication is successful and the user has the correct role
            login(request, user)
            return redirect('personal-dashboard')
        else:
            # Returning an error message if authentication fails or the user has the wrong role
            error_message = "Invalid credentials or unauthorized role."
            return render(request, 'authentication/customers-login/personal-login.html', {'error_message': error_message})

    return render(request, 'authentication/customers-login/personal-login.html')

# BUSINESS ACCOUNT LOGIN
def business_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticating the user
        user = authenticate(request, username=email, password=password)

        if user and user.role == UserModel.Role.BUSINESS_ACCOUNTS:
            # Logging the user in if authentication is successful and the user has the correct role
            login(request, user)
            return redirect('business-dashboard')
        else:
            # Returning an error message if authentication fails or the user has the wrong role
            error_message = "Invalid credentials or unauthorized role."
            return render(request, 'authentication/customers-login/business-login.html', {'error_message': error_message})

    return render(request, 'authentication/customers-login/business-login.html')


def investor_login_view(request):
    # View function for investor account login
    return render(request, 'authentication/customers-login/invest-login.html')


# ADMIN ACCOUNT REGISTRATION
def admin_registration_view(request):
    if request.method == 'POST':
        fullname = request.POST.get('fname')
        email = request.POST.get('email')
        user_password = request.POST.get('password')
        user_address = request.POST.get('address')
        user_address2 = request.POST.get('address2')
        user_city = request.POST.get('city')
        user_state = request.POST.get('state')
        user_zipcode = request.POST.get('zipcode')

        # Hashing the password
        hashed_password = make_password(user_password)

        new_admin = UserModel.objects.create_user(
            email=email,
            password=hashed_password,
            role=UserModel.Role.ADMIN,
            fullname=fullname,
            user_address=user_address,
            user_address2=user_address2,
            user_city=user_city,
            user_state=user_state,
            user_zipcode=user_zipcode
        )

        return redirect('admin-login')

    return render(request, 'authentication/admin/admin-reg.html')


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
