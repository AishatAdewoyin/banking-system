from django.urls import path
from views import businessRegView
from views import investorRegView


from django.urls import path
from .views import BusinessRegView, PersonalFullnameValidationView

urlpatterns = [
    path('register/', BusinessRegView.as_view(), name='register'),
    path('fullname_validation/', PersonalFullnameValidationView.as_view(), name='fullname_validation'),
]

