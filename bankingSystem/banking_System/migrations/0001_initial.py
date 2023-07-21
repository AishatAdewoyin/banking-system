# Generated by Django 4.2.2 on 2023-07-21 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('user_password', models.CharField(max_length=255)),
                ('user_address', models.CharField(max_length=255)),
                ('user_address2', models.CharField(max_length=255)),
                ('user_city', models.CharField(max_length=255)),
                ('user_state', models.CharField(max_length=255)),
                ('user_zipcode', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'business_account_reg',
            },
        ),
        migrations.CreateModel(
            name='InvestorAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('user_password', models.CharField(max_length=255)),
                ('user_address', models.CharField(max_length=255)),
                ('user_address2', models.CharField(max_length=255)),
                ('user_city', models.CharField(max_length=255)),
                ('user_state', models.CharField(max_length=255)),
                ('user_zipcode', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'investors_account_reg',
            },
        ),
        migrations.CreateModel(
            name='PersonalAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('user_password', models.CharField(max_length=255)),
                ('user_address', models.CharField(max_length=255)),
                ('user_address2', models.CharField(max_length=255)),
                ('user_city', models.CharField(max_length=255)),
                ('user_state', models.CharField(max_length=255)),
                ('user_zipcode', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'personal_account_reg',
            },
        ),
    ]
