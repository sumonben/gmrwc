# Generated by Django 5.1 on 2024-08-24 03:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0005_navelement_navitem_page_navelement_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('body', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='media/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('published', models.DateTimeField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='navelement',
            name='page',
        ),
        migrations.CreateModel(
            name='ServiceBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('element', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontpage.page')),
            ],
        ),
        migrations.AddField(
            model_name='navelement',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontpage.page'),
        ),
    ]
