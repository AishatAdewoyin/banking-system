from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

# Admin
class AdminAccountRegistrationForm(UserCreationForm):
    # Form for Admin account registration
    class Meta:
        model = User
        fields = ['email', 'fullname', 'password1', 'password2']

# Personal
class PersonalAccountRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'fullname', 'user_address', 'user_address2', 'password1', 'password2','user_city', 'user_state', 'user_zipcode']

# Business
class BusinessAccountRegistrationForm(UserCreationForm):
    # Form for Business account registration
    class Meta:
        model = User
        fields = ['email', 'fullname', 'user_address', 'user_address2', 'password1', 'password2','user_city', 'user_state', 'user_zipcode']

# Investor
class InvestorAccountRegistrationForm(UserCreationForm):
    # Form for Investor account registration

    class Meta:
        model = User
        fields = ['email', 'fullname', 'user_address', 'user_address2', 'password1', 'password2','user_city', 'user_state', 'user_zipcode']
