# Generated by Django 5.1.3 on 2024-11-15 03:47

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0022_alter_subject_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='navdepartmentelement',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='navdepartmentelement',
            name='body_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='type',
            field=models.CharField(blank=True, choices=[('Major', 'Major'), ('Compulsory', 'Compulsory'), ('Non-Major', 'Non-Major'), ('Fourth', 'Fourth'), ('Optional', 'Optional')], max_length=25, null=True),
        ),
    ]
