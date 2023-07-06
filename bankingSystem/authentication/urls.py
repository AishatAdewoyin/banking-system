from django.urls import path
from .views import PersonalFullnameValidationView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('fullname_validation/', csrf_exempt(PersonalFullnameValidationView.as_view()), name='fullname_validation'),
]
