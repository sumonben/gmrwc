# Generated by Django 5.1 on 2024-09-02 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0016_alter_page_type_alter_teacher_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='serial',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='department',
            name='serial',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='navelement',
            name='serial',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='navitem',
            name='serial',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='page',
            name='serial',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='post',
            name='serial',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='servicebox',
            name='serial',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='page',
            name='type',
            field=models.CharField(choices=[('1', 'static'), ('2', 'dynamic'), ('3', 'link'), ('4', 'department')], default='1', max_length=25),
        ),
    ]
