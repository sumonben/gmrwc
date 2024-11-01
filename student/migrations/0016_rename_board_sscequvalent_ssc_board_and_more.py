# Generated by Django 5.1 on 2024-10-31 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_alter_student_user_alter_studentadmission_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sscequvalent',
            old_name='board',
            new_name='ssc_board',
        ),
        migrations.RenameField(
            model_name='sscequvalent',
            old_name='cgpa_with_4th',
            new_name='ssc_cgpa_with_4th',
        ),
        migrations.RenameField(
            model_name='sscequvalent',
            old_name='cgpa_without_4th',
            new_name='ssc_cgpa_without_4th',
        ),
        migrations.RenameField(
            model_name='sscequvalent',
            old_name='exam_roll',
            new_name='ssc_exam_roll',
        ),
        migrations.RenameField(
            model_name='sscequvalent',
            old_name='group',
            new_name='ssc_group',
        ),
        migrations.RenameField(
            model_name='sscequvalent',
            old_name='passing_year',
            new_name='ssc_passing_year',
        ),
        migrations.RenameField(
            model_name='sscequvalent',
            old_name='regitration_no',
            new_name='ssc_regitration_no',
        ),
        migrations.RenameField(
            model_name='sscequvalent',
            old_name='session',
            new_name='ssc_session',
        ),
    ]
