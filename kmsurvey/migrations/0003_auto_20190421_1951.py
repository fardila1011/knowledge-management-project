# Generated by Django 2.2 on 2019-04-21 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kmsurvey', '0002_auto_20190421_1932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dicotomic_choice',
            old_name='dicotomic_choice',
            new_name='dicotomic_choice_value',
        ),
        migrations.RenameField(
            model_name='scale_choice',
            old_name='scale_choice',
            new_name='scale_choice_value',
        ),
        migrations.AddField(
            model_name='dicotomic_choice',
            name='dicotomic_choice_txt',
            field=models.CharField(default='null', max_length=5),
        ),
        migrations.AddField(
            model_name='scale_choice',
            name='scale_choice_txt',
            field=models.CharField(default='null', max_length=30),
        ),
    ]
