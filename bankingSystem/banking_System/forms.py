from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import NewUser

# Admin
class AdminAccountRegistrationForm(UserCreationForm):
    # Form for Admin account registration
    class Meta:
        model = NewUser
        fields = ['email', 'fullname', 'password1', 'password2']

# Personal
class PersonalAccountRegistrationForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ['email', 'fullname', 'user_address', 'user_address2', 'password1', 'password2','user_city', 'user_state', 'user_zipcode']

# Business
class BusinessAccountRegistrationForm(UserCreationForm):
    # Form for Business account registration
    class Meta:
        model = NewUser
        fields = ['email', 'fullname', 'user_address', 'user_address2', 'password1', 'password2','user_city', 'user_state', 'user_zipcode']

# Investor
class InvestorAccountRegistrationForm(UserCreationForm):
    # Form for Investor account registration

    class Meta:
        model = NewUser
        fields = ['email', 'fullname', 'user_address', 'user_address2', 'password1', 'password2','user_city', 'user_state', 'user_zipcode']


############## LOGINS ############

class AdminAccountLoginForm(forms.ModelForm):
    password=forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = NewUser
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            password=self.clean_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError("invalid Credentials")


class PersonalAccountLoginForm(forms.ModelForm):
    password=forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = NewUser
        fields = ('email', 'fullname', 'password')

    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            fullname=self.cleaned_data['fullname']
            password=self.clean_data['password']

            if not authenticate(email=email, fullname=fullname, password=password):
                raise forms.ValidationError("invalid Credentials")

            

class BusinessAccountLoginForm(forms.ModelForm):
    password=forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = NewUser
        fields = ('email', 'fullname', 'password')

    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            fullname=self.cleaned_data['fullname']
            password=self.clean_data['password']

            if not authenticate(email=email, fullname=fullname, password=password):
                raise forms.ValidationError("invalid Credentials")



class InvestorsAccountLoginForm(forms.ModelForm):
    password=forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = NewUser
        fields = ('email', 'fullname', 'password')

    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            fullname=self.cleaned_data['fullname']
            password=self.clean_data['password']

            if not authenticate(email=email, fullname=fullname, password=password):
                raise forms.ValidationError("invalid Credentials")