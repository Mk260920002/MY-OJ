# Generated by Django 4.0.5 on 2022-07-06 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_App', '0003_submissions_verdict_submissions_problem_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
