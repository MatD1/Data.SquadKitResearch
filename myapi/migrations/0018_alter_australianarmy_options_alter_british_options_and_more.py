# Generated by Django 4.0.4 on 2022-05-22 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0017_alter_insurgent_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='australianarmy',
            options={'verbose_name_plural': 'Australian Army'},
        ),
        migrations.AlterModelOptions(
            name='british',
            options={'verbose_name_plural': 'British'},
        ),
        migrations.AlterModelOptions(
            name='canadianarmy',
            options={'verbose_name_plural': 'Canadian Army'},
        ),
        migrations.AlterModelOptions(
            name='irregularmilitia',
            options={'verbose_name_plural': 'Irregular Militia'},
        ),
        migrations.AlterModelOptions(
            name='middleeasternalliance',
            options={'verbose_name_plural': 'Middle Eastern Alliance'},
        ),
        migrations.AlterModelOptions(
            name='panasia',
            options={'verbose_name_plural': 'Pan-Asia'},
        ),
        migrations.AlterModelOptions(
            name='russiangroundforces',
            options={'verbose_name_plural': 'Russian Ground Forces'},
        ),
        migrations.AlterModelOptions(
            name='unitedstatesarmy',
            options={'verbose_name_plural': 'United States Army'},
        ),
        migrations.AlterModelOptions(
            name='unitedstatesmarinecore',
            options={'verbose_name_plural': 'United States Marine Core'},
        ),
    ]
