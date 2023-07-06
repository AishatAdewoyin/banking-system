from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),
    path('banking-system/', include('banking_system.urls')),
    # Add more URL patterns for your project here
]


