# Generated by Django 4.1.2 on 2022-10-25 10:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('creator_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('option_1', models.CharField(max_length=50)),
                ('option_2', models.CharField(max_length=50)),
                ('option_3', models.CharField(max_length=50)),
                ('option_4', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=20)),
                ('duration', models.TimeField(default=datetime.datetime(2022, 10, 25, 10, 21, 22, 122494))),
                ('fk_course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
        migrations.CreateModel(
            name='TestAppeared',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('score', models.IntegerField(default=0)),
                ('fk_test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.test')),
                ('fk_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SelectedAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=100)),
                ('fk_question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.question')),
                ('fk_test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.test')),
                ('fk_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='fk_test_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.test'),
        ),
    ]
