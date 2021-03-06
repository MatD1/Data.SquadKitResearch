# Generated by Django 4.0.4 on 2022-05-16 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0006_rename_middleeasteralliance_middleeasternalliance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='australianarmy',
            name='RoleName',
            field=models.CharField(default='N/A', max_length=60, unique=True, verbose_name='Role Name'),
        ),
        migrations.AlterField(
            model_name='british',
            name='RoleName',
            field=models.CharField(default='N/A', max_length=60, unique=True, verbose_name='Role Name'),
        ),
        migrations.AlterField(
            model_name='canadianarmy',
            name='RoleName',
            field=models.CharField(default='N/A', max_length=60, unique=True, verbose_name='Role Name'),
        ),
        migrations.AlterField(
            model_name='insurgent',
            name='RoleName',
            field=models.CharField(default='N/A', max_length=60, unique=True, verbose_name='Role Name'),
        ),
        migrations.AlterField(
            model_name='irregularmilitia',
            name='RoleName',
            field=models.CharField(default='N/A', max_length=60, unique=True, verbose_name='Role Name'),
        ),
        migrations.AlterField(
            model_name='middleeasternalliance',
            name='RoleName',
            field=models.CharField(default='N/A', max_length=60, unique=True, verbose_name='Role Name'),
        ),
        migrations.AlterField(
            model_name='panasia',
            name='RoleName',
            field=models.CharField(default='N/A', max_length=60, unique=True, verbose_name='Role Name'),
        ),
        migrations.AlterField(
            model_name='russiangroundforces',
            name='RoleName',
            field=models.CharField(default='N/A', max_length=60, unique=True, verbose_name='Role Name'),
        ),
        migrations.AlterField(
            model_name='unitedstatesarmy',
            name='RoleName',
            field=models.CharField(default='N/A', max_length=60, unique=True, verbose_name='Role Name'),
        ),
        migrations.AlterField(
            model_name='unitedstatesarmy',
            name='thirdSlot',
            field=models.CharField(default='N/A', max_length=30, unique=True, verbose_name='Third Equipment Slot'),
        ),
        migrations.AlterField(
            model_name='unitedstatesmarinecore',
            name='RoleName',
            field=models.CharField(default='N/A', max_length=60, unique=True, verbose_name='Role Name'),
        ),
    ]
