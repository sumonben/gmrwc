# Generated by Django 5.1 on 2024-10-28 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0007_alter_subject_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='type',
            field=models.CharField(blank=True, choices=[('Major', 'Major'), ('Non-Major', 'Non-Major'), ('Compulsory', 'Compulsory'), ('Fourth', 'Fourth'), ('Optional', 'Optional')], max_length=25, null=True),
        ),
    ]