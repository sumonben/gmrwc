# Generated by Django 5.1 on 2024-11-13 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0016_alter_subject_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='type',
            field=models.CharField(blank=True, choices=[('Compulsory', 'Compulsory'), ('Major', 'Major'), ('Non-Major', 'Non-Major'), ('Optional', 'Optional'), ('Fourth', 'Fourth')], max_length=25, null=True),
        ),
    ]
