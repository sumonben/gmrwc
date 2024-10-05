# Generated by Django 5.1 on 2024-10-05 11:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='lattitude',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='longitude',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.CreateModel(
            name='Upazilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('name_en', models.CharField(max_length=25, unique=True)),
                ('link', models.CharField(blank=True, max_length=15, null=True)),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.district')),
            ],
        ),
        migrations.CreateModel(
            name='Union',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('name_en', models.CharField(max_length=25, unique=True)),
                ('link', models.CharField(blank=True, max_length=15, null=True)),
                ('upazilla', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.upazilla')),
            ],
        ),
    ]