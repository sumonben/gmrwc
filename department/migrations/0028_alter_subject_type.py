# Generated by Django 5.1.3 on 2024-11-15 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0027_alter_subject_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='type',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
