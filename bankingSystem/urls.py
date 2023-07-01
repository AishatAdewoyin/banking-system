from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # ... other URL patterns ...
    path('bankingsystem/', include('bankingSystem.urls')),
    path('admin/', admin.site.urls),
]

