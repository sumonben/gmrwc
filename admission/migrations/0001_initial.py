# Generated by Django 5.1 on 2024-10-14 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(default=10)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('title_en', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
            options={
                'ordering': ['serial'],
            },
        ),
    ]