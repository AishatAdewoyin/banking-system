from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='user_address2',
            field=models.CharField(max_length=255, verbose_name='address 2'),
        ),
    ]