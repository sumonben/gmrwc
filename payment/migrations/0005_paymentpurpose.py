# Generated by Django 5.1.3 on 2024-11-27 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_alter_transaction_tran_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentPurpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(default=10)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('title_en', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Payment Purpose',
                'verbose_name_plural': 'Payment Purpose',
                'ordering': ['serial'],
            },
        ),
    ]