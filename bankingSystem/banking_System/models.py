from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, fullname, password=None):
        if not email:
            raise ValueError("Email Required")
        if not fullname:
            raise ValueError("Full Name Required")

        user=self.model(
            email=self.normalize_email(email),
            fullname=fullname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fullname, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            fullname=fullname,
            password=password
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
     #Custom user model extending AbstractUser
     email = models.EmailField(verbose_name="email address", max_length=60, unique=True)
     fullname = models.CharField(verbose_name="full name", max_length=255, unique=True)
     user_address = models.CharField(max_length=255)
     user_address2 = models.CharField(max_length=255)
     user_city = models.CharField(max_length=255)
     user_state = models.CharField(max_length=255)
     user_zipcode = models.CharField(max_length=10)
     date_joined=models.DateTimeField(auto_now_add=True)
     date_login=models.DateTimeField(auto_now_add=True)
     is_admin=models.BooleanField(default=False)
     is_active=models.BooleanField(default=True)
     is_staff=models.BooleanField(default=False)
     is_superuser=models.BooleanField(default=False)

     USERNAME_FIELD="email"
     REQUIRED_FIELDS=["fullname"]

     objects=UserManager()

     def __str__(self):
         return self.fullname

     def has_perm(self, perm, obj=None):
         return True

     def has_module_perms(self, app_label):
         return True

    
    

#     # user_address = models.CharField(max_length=255)
#     # user_address2 = models.CharField(max_length=255)
#     # user_city = models.CharField(max_length=255)
#     # user_state = models.CharField(max_length=255)
#     # user_zipcode = models.CharField(max_length=10)

#     class Role(models.TextChoices):
#         # Enum choices for user roles
#         ADMIN = "ADMIN", 'Admin'
#         PERSONAL_ACCOUNTS = "PERSONALACCOUNTS", 'PersonalAccounts'
#         BUSINESS_ACCOUNTS = "BUSINESSACCOUNTS", 'BusinessAccounts'
#         INVESTORS_ACCOUNTS = "INVESTORSACCOUNTS", 'InvestorsAccounts'

#     role = models.CharField(max_length=20, choices=Role.choices, default=Role.ADMIN)

#     objects = CustomUserManager()

#     def save(self, *args, **kwargs):
#         # Set the default role for new users to ADMIN
#         if not self.pk:
#             self.role = self.Role.ADMIN
#         return super().save(*args, **kwargs)

#     def __str__(self):
#         return self.fullname

# class BusinessAccount(models.Model):
#     # Model for BusinessAccount with specific fields
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='business_account')
#     fullname = models.CharField(max_length=255)
#     user_address = models.CharField(max_length=255)
#     user_address2 = models.CharField(max_length=255)
#     user_city = models.CharField(max_length=255)
#     user_state = models.CharField(max_length=255)
#     user_zipcode = models.CharField(max_length=10)

# class PersonalAccount(models.Model):
#     # Model for PersonalAccount with specific fields
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='personal_account')
#     fullname = models.CharField(max_length=255)
#     user_address = models.CharField(max_length=255)
#     user_address2 = models.CharField(max_length=255)
#     user_city = models.CharField(max_length=255)
#     user_state = models.CharField(max_length=255)
#     user_zipcode = models.CharField(max_length=10)

# class InvestorAccount(models.Model):
#     # Model for InvestorAccount with specific fields
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='investor_account')
#     fullname = models.CharField(max_length=255)
#     user_address = models.CharField(max_length=255)
#     user_address2 = models.CharField(max_length=255)
#     user_city = models.CharField(max_length=255)
#     user_state = models.CharField(max_length=255)
#     user_zipcode = models.CharField(max_length=10)
