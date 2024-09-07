# Generated by Django 5.1 on 2024-09-07 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_student_name_bangla_teacher_name_bangla_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='batch',
            field=models.CharField(choices=[('0', '---বিসিএস ব্যাচ---'), ('1', 'প্রযোজ্য নয়'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '66'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50')], default='0', max_length=25),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='designation',
            field=models.CharField(choices=[('0', '---পদবী---'), ('1', 'অধ্যাপক'), ('2', 'সহযোগী অধ্যাপক'), ('3', 'সহকারী অধ্যাপক'), ('4', 'প্রভাষক'), ('5', 'প্রদর্শক'), ('6', 'শরীরচর্চা শিক্ষক'), ('7', 'শিক্ষক'), ('8', 'প্রদর্শক(অনিয়মিত)')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
