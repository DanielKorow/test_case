# Generated by Django 3.1 on 2020-08-07 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testcase', '0008_answer_survey_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='survey',
        ),
    ]