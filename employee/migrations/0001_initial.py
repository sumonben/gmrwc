# Generated by Django 5.1.3 on 2024-12-07 04:15

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0029_alter_department_about_en_alter_department_name_en'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(default=10, verbose_name='পদক্রম')),
                ('emloyee_name', models.CharField(max_length=100, verbose_name='নাম(ইংরেজি)')),
                ('emloyee_name_bangla', models.CharField(blank=True, max_length=100, null=True, verbose_name='নাম (বাংলা)')),
                ('emloyee_email', models.EmailField(max_length=50, unique=True, verbose_name='ই-মেইল')),
                ('emloyee_phone', models.CharField(max_length=11, unique=True, verbose_name='মোবাইল নং')),
                ('designation', models.CharField(blank=True, choices=[('0', '---পদবী---'), ('1', 'অফিস সহকারী'), ('2', 'কম্পিউটার অপারেটর'), ('3', 'ড্রাইভার'), ('4', 'অফিস সহায়ক'), ('5', 'পরিছন্নতা কর্মী'), ('6', '')], max_length=100, null=True, verbose_name='পদবী')),
                ('position', models.CharField(blank=True, choices=[('1', 'অধ্যক্ষ'), ('2', 'উপাধ্যক্ষ'), ('3', 'সম্পাদক (শিক্ষক পরিষদ)'), ('4', 'বিভাগীয় প্রধান'), ('5', 'শিক্ষক'), ('6', 'কর্মকর্তা'), ('অন্যান্য', 'অন্যান্য')], max_length=100, null=True, verbose_name='পদ')),
                ('service_id', models.CharField(max_length=25, verbose_name='সার্ভিস আইডি')),
                ('emloyee_type', models.CharField(blank=True, choices=[('1', 'নিয়মিত'), ('2', 'অনিয়মিত')], max_length=100, null=True, verbose_name='কর্মচারীর ধরণ')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='জন্ম তারিখ')),
                ('first_joining_date', models.DateField(blank=True, null=True, verbose_name='প্রথম যোগদানের তারিখ')),
                ('joining_date', models.DateField(blank=True, null=True, verbose_name='যোগদানের তারিখ')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='রিলিজের তারিখ')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='ছবি')),
                ('signature', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='স্বাক্ষর')),
                ('bio', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='জীবনী (বাংলা)')),
                ('bio_en', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='জীবনী ইংরেজি')),
                ('is_active', models.BooleanField(default=False, verbose_name='সক্রিয় কিনা?')),
                ('branch', models.ManyToManyField(blank=True, null=True, to='department.branch', verbose_name='শাখা')),
                ('emloyee_department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='department.department', verbose_name='বিভাগ')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['serial'],
            },
        ),
    ]
