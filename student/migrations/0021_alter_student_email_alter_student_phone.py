# Generated by Django 5.1.3 on 2024-11-29 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0020_transaction_email_transaction_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=11),
        ),
    ]
