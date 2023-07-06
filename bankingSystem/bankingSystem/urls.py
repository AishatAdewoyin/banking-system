from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # ... other URL patterns ...
    # path('bankingSystem/', include('bankingSystem.urls')),
    # path('authentication/', include('authentication.urls')),
    path('admin/', admin.site.urls),
]


