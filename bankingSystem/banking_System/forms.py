from django import forms
from .models import User

# admin
class AdminAccountRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Abc123@# (Letters, Numbers, and symbols required. Not more than 18 characters)'}))

    class Meta:
        model = User
        fields = ['fullname', 'email', 'password']

# Personal
class PersonalAccountRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Abc123@# (Letters, Numbers, and symbols required. Not more than 18 characters)'}))

    class Meta:
        model = User
        fields = ['fullname', 'email', 'password', 'user_address', 'user_address2', 'user_city', 'user_state', 'user_zipcode']


# Business 
class BusinessAccountRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Abc123@# (Letters, Numbers, and symbols required. Not more than 18 characters)'}))

    class Meta:
        model = User
        fields = ['fullname', 'email', 'password', 'user_address', 'user_address2', 'user_city', 'user_state', 'user_zipcode']


# Investor
class InvestorAccountRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Abc123@# (Letters, Numbers, and symbols required. Not more than 18 characters)'}))

    class Meta:
        model = User
        fields = ['fullname', 'email', 'password', 'user_address', 'user_address2', 'user_city', 'user_state', 'user_zipcode']
