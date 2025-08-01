# Generated by Django 5.1.3 on 2025-07-25 17:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
        ('payment', '__first__'),
        ('student', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_bangla', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=11, null=True)),
                ('father_name', models.CharField(max_length=100)),
                ('father_name_bangla', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_name', models.CharField(max_length=100)),
                ('mother_name_bangla', models.CharField(blank=True, max_length=100, null=True)),
                ('section', models.CharField(blank=True, max_length=25, null=True)),
                ('class_roll', models.CharField(blank=True, max_length=11, null=True)),
                ('exam_roll', models.CharField(blank=True, max_length=25, null=True)),
                ('registration', models.CharField(blank=True, max_length=25, null=True)),
                ('cgpa', models.CharField(blank=True, max_length=15, null=True)),
                ('passing_year', models.CharField(blank=True, max_length=25, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=15, null=True)),
                ('certificate_type', models.CharField(blank=True, max_length=15, null=True)),
                ('session_key', models.CharField(blank=True, max_length=100, null=True)),
                ('is_valid', models.BooleanField(default=False)),
                ('adress', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.adress')),
                ('class_year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='department.class')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='department.department')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='department.group')),
                ('session', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='department.session')),
                ('student_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.studentcategory')),
                ('subjects', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.subjectchoice')),
                ('transaction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payment.transaction')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
