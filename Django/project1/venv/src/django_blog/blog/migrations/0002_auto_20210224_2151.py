# Generated by Django 3.1.5 on 2021-02-24 21:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 24, 21, 51, 21, 922356, tzinfo=utc)),
        ),
    ]
