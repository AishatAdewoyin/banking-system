from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Custom user manager for creating regular users
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Custom user manager for creating superusers (admin)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    # Custom user model extending AbstractUser
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=255)
    user_address = models.CharField(max_length=255)
    user_address2 = models.CharField(max_length=255)
    user_city = models.CharField(max_length=255)
    user_state = models.CharField(max_length=255)
    user_zipcode = models.CharField(max_length=10)

    class Role(models.TextChoices):
        # Enum choices for user roles
        ADMIN = "ADMIN", 'Admin'
        PERSONAL_ACCOUNTS = "PERSONALACCOUNTS", 'PersonalAccounts'
        BUSINESS_ACCOUNTS = "BUSINESSACCOUNTS", 'BusinessAccounts'
        INVESTORS_ACCOUNTS = "INVESTORSACCOUNTS", 'InvestorsAccounts'

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.ADMIN)

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        # Set the default role for new users to ADMIN
        if not self.pk:
            self.role = self.Role.ADMIN
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.fullname

class BusinessAccount(models.Model):
    # Model for BusinessAccount with specific fields
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='business_account')
    fullname = models.CharField(max_length=255)
    user_address = models.CharField(max_length=255)
    user_address2 = models.CharField(max_length=255)
    user_city = models.CharField(max_length=255)
    user_state = models.CharField(max_length=255)
    user_zipcode = models.CharField(max_length=10)

class PersonalAccount(models.Model):
    # Model for PersonalAccount with specific fields
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='personal_account')
    fullname = models.CharField(max_length=255)
    user_address = models.CharField(max_length=255)
    user_address2 = models.CharField(max_length=255)
    user_city = models.CharField(max_length=255)
    user_state = models.CharField(max_length=255)
    user_zipcode = models.CharField(max_length=10)

class InvestorAccount(models.Model):
    # Model for InvestorAccount with specific fields
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='investor_account')
    fullname = models.CharField(max_length=255)
    user_address = models.CharField(max_length=255)
    user_address2 = models.CharField(max_length=255)
    user_city = models.CharField(max_length=255)
    user_state = models.CharField(max_length=255)
    user_zipcode = models.CharField(max_length=10)
