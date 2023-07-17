from django.db import models

# personal account reg
class PersonalAccount(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    user_password = models.CharField(max_length=255)
    user_address = models.CharField(max_length=255)
    user_address2 = models.CharField(max_length=255)
    user_city = models.CharField(max_length=255)
    user_state = models.CharField(max_length=255)
    user_zipcode = models.CharField(max_length=10)

    class Meta:
        db_table = 'personal_account_reg'

# business account reg 
class BusinessAccount(models.Model):
    class Meta:
        db_table = 'business_account_reg'

# investor account reg
class InvestorAccount(models.Model):
    class Meta:
        db_table = 'investors_account_reg'



# from django.db import models

# class Account(models.Model):
#     account_number = models.CharField(max_length=50)
#     # Add other fields as needed

# class Transaction(models.Model):
#     account = models.ForeignKey(Account, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     # Add other fields as needed
