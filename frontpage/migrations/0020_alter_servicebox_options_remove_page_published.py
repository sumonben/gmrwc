# Generated by Django 5.1 on 2024-09-21 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0019_remove_teacher_branch_remove_teacher_department_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicebox',
            options={'ordering': ['serial']},
        ),
        migrations.RemoveField(
            model_name='page',
            name='published',
        ),
    ]
