# from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('banking_system/', include('banking_system.urls')),
    # Other URL patterns for other apps, if any
]


