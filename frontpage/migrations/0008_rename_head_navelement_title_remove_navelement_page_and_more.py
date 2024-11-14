# Generated by Django 5.1 on 2024-08-24 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0007_remove_servicebox_element_servicebox_element'),
    ]

    operations = [
        migrations.RenameField(
            model_name='navelement',
            old_name='head',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='navelement',
            name='page',
        ),
        migrations.AddField(
            model_name='navelement',
            name='page',
            field=models.ManyToManyField(blank=True, null=True, to='frontpage.page'),
        ),
    ]
