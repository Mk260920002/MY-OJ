# Generated by Django 4.0.5 on 2022-07-06 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('My_App', '0002_problem_remove_submissions_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissions',
            name='Verdict',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='submissions',
            name='problem_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='My_App.problem'),
            preserve_default=False,
        ),
    ]
