# Generated by Django 3.1 on 2020-08-07 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testcase', '0002_auto_20200806_1635'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer_choice',
            new_name='answer',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='answer_text',
        ),
    ]
