# Generated by Django 4.0.4 on 2022-05-22 13:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0018_alter_australianarmy_options_alter_british_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alerts',
            options={'verbose_name_plural': 'Alerts'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Posts'},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='createdat',
            new_name='createdAt',
        ),
        migrations.RemoveField(
            model_name='alerts',
            name='createdat',
        ),
        migrations.AddField(
            model_name='alerts',
            name='createdAt',
            field=models.DateTimeField(auto_now=True, verbose_name=datetime.datetime.now),
        ),
    ]
