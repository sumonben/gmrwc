# Generated by Django 5.1 on 2024-09-04 03:16

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('department', '0003_branch_department_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('class_roll', models.CharField(max_length=11)),
                ('session', models.CharField(choices=[('1', '2022-23'), ('2', '2023-24'), ('3', '2024-25'), ('4', '2025-26'), ('5', '2026-27'), ('6', '2027-28 '), ('7', '2028-29'), ('8', '2029-30')], default='4', max_length=100)),
                ('student_category', models.CharField(choices=[('1', 'এইচএসসি'), ('2', 'অনার্স'), ('3', 'মাস্টার্স')], default='1', max_length=100)),
                ('exam_roll', models.CharField(blank=True, max_length=25, null=True)),
                ('registration', models.CharField(blank=True, max_length=25, null=True)),
                ('class_year', models.CharField(choices=[('1', '১ম বর্ষ'), ('2', '২য় বর্ষ'), ('3', '৩য় বর্ষ'), ('4', '৪র্থ বর্ষ'), ('5', '১ম পর্ব'), ('6', 'শেষ পর্ব'), ('7', 'পাশকৃত')], default='1', max_length=100)),
                ('passing_year', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('signature', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='department.department')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('designation', models.CharField(choices=[('1', 'অধ্যাপক'), ('2', 'সহযোগী অধ্যাপক'), ('3', 'সহকারী অধ্যাপক'), ('4', 'প্রভাষক'), ('5', 'প্রদর্শক'), ('6', 'শরীরচর্চা শিক্ষক'), ('7', 'শিক্ষক'), ('8', 'প্রদর্শক(অনিয়মিত)')], default='4', max_length=100)),
                ('position', models.CharField(choices=[('1', 'অধ্যক্ষ'), ('2', 'উপাধ্যক্ষ'), ('3', 'সম্পাদক (শিক্ষক পরিষদ)'), ('4', 'বিভাগীয় প্রধান'), ('5', 'শিক্ষক'), ('6', 'কর্মকর্তা'), ('7', 'অন্যান্য')], default='1', max_length=100)),
                ('service_id', models.CharField(max_length=25)),
                ('batch', models.CharField(choices=[('0', 'প্রযোজ্য নয়'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '66'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50')], default='0', max_length=25)),
                ('merit', models.CharField(blank=True, max_length=25, null=True)),
                ('first_joining_date', models.DateField(blank=True, null=True)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('signature', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('message', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('bio', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('branch', models.ManyToManyField(blank=True, null=True, to='department.branch')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='department.department')),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]