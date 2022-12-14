# Generated by Django 4.1.2 on 2022-10-27 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_alter_test_duration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='fk_test_id',
            new_name='test_related',
        ),
        migrations.RenameField(
            model_name='selectedanswer',
            old_name='fk_user_id',
            new_name='given_by_student',
        ),
        migrations.RenameField(
            model_name='selectedanswer',
            old_name='fk_question_id',
            new_name='question_related',
        ),
        migrations.RenameField(
            model_name='selectedanswer',
            old_name='fk_test_id',
            new_name='test_related',
        ),
        migrations.RenameField(
            model_name='test',
            old_name='fk_course_id',
            new_name='course_related',
        ),
        migrations.RenameField(
            model_name='testappeared',
            old_name='fk_user_id',
            new_name='given_by_student',
        ),
        migrations.RenameField(
            model_name='testappeared',
            old_name='fk_test_id',
            new_name='test_related',
        ),
    ]
