# Generated by Django 5.1.3 on 2024-11-26 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0004_certificate_certificate_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='session_key',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
