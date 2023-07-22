from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.db import models

class User(AbstractUser):
    # User model fields and methods go here
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        PERSONAL_ACCOUNTS = "PERSONALACCOUNTS", 'PersonalAccounts'
        BUSINESS_ACCOUNTS = "BUSINESSACCOUNTS", 'BusinessAccounts'
        INVESTORS_ACCOUNTS = "INVESTORSACCOUNTS", 'InvestorsAccounts'
    class Meta:
        swappable = 'AUTH_USER_MODEL'

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices, default=base_role)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)







# class CustomUserManager(BaseUserManager):
#     def _create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("Kindly provide an email address")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self.create_user(email, password, **extra_fields)

#     def create_superuser(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)

# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(blank=True, default='', unique=True)
#     name = models.CharField(max_length=255, blank=True, default='')

#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)

#     object = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     EMAIL_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'

#     def get_full_name(self):
#         return self.name

#     def get_shortform_name(self):
#         return self.name or self.email.split('@')[0]


# # personal accounts registration

# class PersonalAccount(models.Model):
#     fullname = models.CharField(max_length=255)
#     email = models.EmailField()
#     user_password = models.CharField(max_length=255)
#     user_address = models.CharField(max_length=255)
#     user_address2 = models.CharField(max_length=255)
#     user_city = models.CharField(max_length=255)
#     user_state = models.CharField(max_length=255)
#     user_zipcode = models.CharField(max_length=10)

#     class Meta:
#         db_table = 'personal_account_reg'


# # business accounts registration

# class BusinessAccount(models.Model):
#     fullname = models.CharField(max_length=255)
#     email = models.EmailField()
#     user_password = models.CharField(max_length=255)
#     user_address = models.CharField(max_length=255)
#     user_address2 = models.CharField(max_length=255)
#     user_city = models.CharField(max_length=255)
#     user_state = models.CharField(max_length=255)
#     user_zipcode = models.CharField(max_length=10)

#     class Meta:
#         db_table = 'business_account_reg'


# # investors accounts registration

# class InvestorAccount(models.Model):
#     fullname = models.CharField(max_length=255)
#     email = models.EmailField()
#     user_password = models.CharField(max_length=255)
#     user_address = models.CharField(max_length=255)
#     user_address2 = models.CharField(max_length=255)
#     user_city = models.CharField(max_length=255)
#     user_state = models.CharField(max_length=255)
#     user_zipcode = models.CharField(max_length=10)

#     class Meta:
#         db_table = 'investors_account_reg'




# from django.db import models

# class Account(models.Model):
#     account_number = models.CharField(max_length=50)
#     # Add other fields as needed

# class Transaction(models.Model):
#     account = models.ForeignKey(Account, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     # Add other fields as needed
