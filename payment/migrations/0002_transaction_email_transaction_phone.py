# Generated by Django 5.1 on 2024-11-18 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True),
        ),
    ]
