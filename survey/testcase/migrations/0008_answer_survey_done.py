# Generated by Django 3.1 on 2020-08-07 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testcase', '0007_survey_relevant'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='survey_done',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='testcase.surveysdone'),
            preserve_default=False,
        ),
    ]
