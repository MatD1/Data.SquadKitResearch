# Generated by Django 4.0.4 on 2022-05-17 04:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0008_australianarmy_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alerts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('body', models.TextField(max_length=200)),
                ('createdat', models.DateTimeField(verbose_name=datetime.datetime.now)),
            ],
        ),
    ]
