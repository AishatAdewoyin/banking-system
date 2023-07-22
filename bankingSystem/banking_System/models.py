from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        PERSONAL_ACCOUNTS = "PERSONALACCOUNTS", 'PersonalAccounts'
        BUSINESS_ACCOUNTS = "BUSINESSACCOUNTS", 'BusinessAccounts'
        INVESTORS_ACCOUNTS = "INVESTORSACCOUNTS", 'InvestorsAccounts'

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices, default=base_role)

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)


class PersonalAccount(User):
    # Add other fields specific to PersonalAccount
    fullname = models.CharField(max_length=255)
    user_address = models.CharField(max_length=255)
    user_address2 = models.CharField(max_length=255)
    user_city = models.CharField(max_length=255)
    user_state = models.CharField(max_length=255)
    user_zipcode = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.Role.PERSONAL_ACCOUNTS
        return super().save(*args, **kwargs)


class BusinessAccount(User):
    # Add other fields specific to BusinessAccount
    fullname = models.CharField(max_length=255)
    user_address = models.CharField(max_length=255)
    user_address2 = models.CharField(max_length=255)
    user_city = models.CharField(max_length=255)
    user_state = models.CharField(max_length=255)
    user_zipcode = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.Role.BUSINESS_ACCOUNTS
        return super().save(*args, **kwargs)


class InvestorAccount(User):
    # Add other fields specific to InvestorAccount
    fullname = models.CharField(max_length=255)
    user_address = models.CharField(max_length=255)
    user_address2 = models.CharField(max_length=255)
    user_city = models.CharField(max_length=255)
    user_state = models.CharField(max_length=255)
    user_zipcode = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.Role.INVESTORS_ACCOUNTS
        return super().save(*args, **kwargs)
