from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from banking_system.models import NewUser

class NewUserAdmin(BaseUserAdmin):
    list_display = (
        'email',
        'fullname',
        'user_address',
        'user_address2',
        'user_city',
        'user_state',
        'user_zipcode',
        'date_joined',
        'last_login',
        'is_admin',
        'is_active',
        'is_staff',
        'is_personal',
        'is_business',
        'is_investor',
        'is_superuser',
    )

    search_fields = (
        'email',
        'fullname',
    )

    readonly_fields = (
        'date_joined',
        'last_login',
    )

    list_filter = ('last_login',)

    fieldsets = ()

    filter_horizontal = ()

    ordering = ('email',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'fullname', 'password1', 'password2'),
        }),
    )
admin.site.register(NewUser, NewUserAdmin)