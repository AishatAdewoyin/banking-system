"""
URL configuration for bankingSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import views

app_name = 'bankingSystem'

urlpatterns = [
    path('', views.index_view, name='index'),  # Home page
    path('customers-reg/personal-reg/', views.personal_registration_view, name='personal-registration'),  # Personal registration
    path('customers-reg/business-reg/', views.business_registration_view, name='business-registration'),  # Business registration
    path('customers-reg/investor-reg/', views.investor_registration_view, name='investor-registration'),  # Investor registration
    path('customers-login/personal-login/', views.personal_login_view, name='personal-login'),  # Personal account login
    path('customers-login/business-login/', views.business_login_view, name='business-login'),  # Business account login
    path('customers-login/investor-login/', views.investor_login_view, name='investor-login'),  # Investor account login
    path('admin-login/', views.admin_login_view, name='admin-login'), # Admin account login
    path('admin/', admin.site.urls),
]

