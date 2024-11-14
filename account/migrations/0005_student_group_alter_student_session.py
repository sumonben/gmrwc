# Generated by Django 5.1 on 2024-09-06 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_student_passing_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='session',
            field=models.CharField(choices=[('0', 'ভর্তি সেশন'), ('1', '2022-23'), ('2', '2023-24'), ('3', '2024-25'), ('4', '2025-26'), ('5', '2026-27'), ('6', '2027-28 '), ('7', '2028-29'), ('8', '2029-30')], default='0', max_length=100),
        ),
    ]
