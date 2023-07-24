from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, fullname, password=None):
        if not email:
            raise ValueError("Email is required")
        if not fullname:
            raise ValueError("Full Name is Required")

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


class NewUser(AbstractBaseUser):
     #Custom user model extending AbstractUser
     email = models.EmailField(verbose_name="Email Address:", max_length=60, unique=True)
     fullname = models.CharField(verbose_name="Your Name, Business Name or Investors Name:", max_length=255, unique=True)
     user_address = models.CharField(verbose_name="address:", max_length=255, unique=True)
     user_address2 = models.CharField(verbose_name="address 2:", max_length=255)
     user_city = models.CharField(verbose_name="city:", max_length=255, unique=True)
     user_state = models.CharField(verbose_name="state:", max_length=255, unique=True)
     user_zipcode = models.CharField(verbose_name="zipcode:", max_length=10, unique=True)
     date_joined=models.DateTimeField(auto_now_add=True)
     last_login=models.DateTimeField(auto_now_add=True)
     is_admin=models.BooleanField(default=False)
     is_active=models.BooleanField(default=True)
     is_staff = models.BooleanField(default=False)
     is_personal=models.BooleanField(default=True)
     is_business=models.BooleanField(default=True)
     is_investor=models.BooleanField(default=True)
     is_superuser=models.BooleanField(default=False)

     USERNAME_FIELD="email"
     REQUIRED_FIELDS=["fullname"]

     objects = UserManager()

     def __str__(self):
         return self.fullname

     def is_personal_user(self):
        return self.is_active and self.is_personal

     def is_business_user(self):
         return self.is_active and self.is_business

     def is_investor_user(self):
        return self.is_active and self.is_investor

     def has_perm(self, perm, obj=None):
         return True

     def has_module_perms(self, app_label):
         return True