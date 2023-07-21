from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.hashers import make_password
from .models import PersonalAccount, BusinessAccount, InvestorAccount


####### AUTHORISATION #######

# THE MAIN PAGE
def index_view(request):
    return render(request, 'index.html')

# PERSONAL ACCOUNT REGISTRATION
@csrf_protect
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

        new_user = PersonalAccount.objects.create(
            fullname=fullname,
            email=email,
            user_password=hashed_password,
            user_address=user_address,
            user_address2=user_address2,
            user_city=user_city,
            user_state=user_state,
            user_zipcode=user_zipcode
        )

        return redirect('personal-login')

    return render(request, 'authentication/customers-reg/personal-reg.html')


# BUSINESS ACCOUNT REGISTRATION
@csrf_protect
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

        new_business = BusinessAccount.objects.create(
            fullname=fullname,
            email=email,
            user_password=hashed_password,
            user_address=user_address,
            user_address2=user_address2,
            user_city=user_city,
            user_state=user_state,
            user_zipcode=user_zipcode
        )

        return redirect('business-login')

    return render(request, 'authentication/customers-reg/business-reg.html')


# INVESTORS ACCOUNT REGISTRATION
@csrf_protect
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

        new_investor = InvestorAccount.objects.create(
            fullname=fullname,
            email=email,
            user_password=hashed_password,
            user_address=user_address,
            user_address2=user_address2,
            user_city=user_city,
            user_state=user_state,
            user_zipcode=user_zipcode
        )

        return redirect('investor-login')

    return render(request, 'authentication/customers-reg/invest-reg.html')




            ########## AUTHENTICATION #########
# # PERSONAL ACCOUNT LOGIN
@csrf_protect
def personal_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user_password = request.POST.get('password')

        # Passing username and password as keyword arguments
        user = authenticate(request, username=email, password=user_password)

        if user is not None:
            login(request, user)
            return redirect('personal-dashboard')

        # elif username is correct but the password is wrong 
        # elif username is wrong but the password is correct 

        else:
            return render(request, 'authentication/customers-login/personal-login.html', {'Error': 'User does not exist'})

    return render(request, 'authentication/customers-login/personal-login.html')


@csrf_protect
def business_login_view(request):
    # View function for business account login
    return render(request, 'authentication/customers-login/business-login.html')

@csrf_protect
def investor_login_view(request):
    # View function for investor account login
    return render(request, 'authentication/customers-login/invest-login.html')

@csrf_protect
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

@csrf_protect
@login_required
def personal_password_reset_view(request):
    # View function for password reset page
    return render(request, 'authentication/customers-reset-password/personal-password-reset.html')

@csrf_protect
def business_password_reset_view(request):
    # View function for business password reset page
    return render(request, 'authentication/customers-reset-password/business-password-reset.html')

@csrf_protect
def investors_password_reset_view(request):
    # View function for investors password reset page
    return render(request, 'authentication/customers-reset-password/investors-password-reset.html')
