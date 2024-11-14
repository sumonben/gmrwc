# Generated by Django 5.1 on 2024-09-04 13:54

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_student_std_id_student_user_teacher_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='passing_year',
            field=models.IntegerField(blank=True, choices=account.models.year_choices, null=True),
        ),
    ]
