# Generated by Django 3.0.5 on 2020-04-29 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='emp_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
