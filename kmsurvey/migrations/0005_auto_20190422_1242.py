# Generated by Django 2.1.7 on 2019-04-22 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kmsurvey', '0004_auto_20190421_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='approach',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kmsurvey.Approach'),
        ),
        migrations.AddField(
            model_name='question',
            name='tool',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kmsurvey.Tool'),
        ),
    ]
