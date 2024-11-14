# Generated by Django 5.1 on 2024-10-04 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0004_branch_name_en_department_name_en'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'ordering': ['serial']},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['serial']},
        ),
        migrations.AddField(
            model_name='department',
            name='assistant_professor',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='department',
            name='associate_professor',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='department',
            name='demonstrator',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='department',
            name='lecturer',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='department',
            name='professor',
            field=models.IntegerField(default=0),
        ),
    ]
