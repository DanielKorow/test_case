# Generated by Django 3.1 on 2020-08-06 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testcase', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='options',
            new_name='option',
        ),
    ]