# Generated by Django 5.1 on 2024-09-30 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_branch_department_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='name_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='name_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]