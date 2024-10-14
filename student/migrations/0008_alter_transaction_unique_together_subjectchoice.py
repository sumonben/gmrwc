# Generated by Django 5.1 on 2024-10-14 08:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0005_alter_branch_options_alter_department_options_and_more'),
        ('student', '0007_guardianinfo_alter_district_options_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='transaction',
            unique_together={('student', 'transactionID')},
        ),
        migrations.CreateModel(
            name='SubjectChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(default=10)),
                ('compulsory_subject', models.ManyToManyField(blank=True, null=True, related_name='compulsory_subject', to='department.department')),
                ('fourth_subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='department.department')),
                ('optional_subject', models.ManyToManyField(blank=True, null=True, related_name='optional_subject', to='department.department')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
            options={
                'ordering': ['serial'],
            },
        ),
    ]