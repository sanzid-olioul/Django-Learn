# Generated by Django 3.1.5 on 2021-02-26 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('height', models.CharField(max_length=8)),
                ('weight', models.FloatField()),
                ('institute', models.CharField(max_length=120)),
            ],
        ),
    ]