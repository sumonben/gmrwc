# Generated by Django 5.1.3 on 2024-11-15 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0026_alter_subject_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='type',
            field=models.CharField(blank=True, choices=[('Fourth', 'Fourth'), ('Non-Major', 'Non-Major'), ('Major', 'Major'), ('Compulsory', 'Compulsory'), ('Optional', 'Optional')], max_length=25, null=True),
        ),
    ]
