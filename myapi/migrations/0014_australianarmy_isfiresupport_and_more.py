# Generated by Django 4.0.4 on 2022-05-18 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0013_insurgent_hasprimary2'),
    ]

    operations = [
        migrations.AddField(
            model_name='australianarmy',
            name='isFireSupport',
            field=models.BooleanField(default=False, verbose_name='Is Role Fire Support?'),
        ),
        migrations.AddField(
            model_name='australianarmy',
            name='isLeadOrCommand',
            field=models.BooleanField(default=False, verbose_name='Is Role Lead or Command?'),
        ),
        migrations.AddField(
            model_name='australianarmy',
            name='isSpecialst',
            field=models.BooleanField(default=False, verbose_name='Is Role Specialst?'),
        ),
        migrations.AddField(
            model_name='british',
            name='isFireSupport',
            field=models.BooleanField(default=False, verbose_name='Is Role Fire Support?'),
        ),
        migrations.AddField(
            model_name='british',
            name='isLeadOrCommand',
            field=models.BooleanField(default=False, verbose_name='Is Role Lead or Command?'),
        ),
        migrations.AddField(
            model_name='british',
            name='isSpecialst',
            field=models.BooleanField(default=False, verbose_name='Is Role Specialst?'),
        ),
        migrations.AddField(
            model_name='canadianarmy',
            name='isFireSupport',
            field=models.BooleanField(default=False, verbose_name='Is Role Fire Support?'),
        ),
        migrations.AddField(
            model_name='canadianarmy',
            name='isLeadOrCommand',
            field=models.BooleanField(default=False, verbose_name='Is Role Lead or Command?'),
        ),
        migrations.AddField(
            model_name='canadianarmy',
            name='isSpecialst',
            field=models.BooleanField(default=False, verbose_name='Is Role Specialst?'),
        ),
        migrations.AddField(
            model_name='insurgent',
            name='isFireSupport',
            field=models.BooleanField(default=False, verbose_name='Is Role Fire Support?'),
        ),
        migrations.AddField(
            model_name='insurgent',
            name='isLeadOrCommand',
            field=models.BooleanField(default=False, verbose_name='Is Role Lead or Command?'),
        ),
        migrations.AddField(
            model_name='insurgent',
            name='isSpecialst',
            field=models.BooleanField(default=False, verbose_name='Is Role Specialst?'),
        ),
        migrations.AddField(
            model_name='irregularmilitia',
            name='isFireSupport',
            field=models.BooleanField(default=False, verbose_name='Is Role Fire Support?'),
        ),
        migrations.AddField(
            model_name='irregularmilitia',
            name='isLeadOrCommand',
            field=models.BooleanField(default=False, verbose_name='Is Role Lead or Command?'),
        ),
        migrations.AddField(
            model_name='irregularmilitia',
            name='isSpecialst',
            field=models.BooleanField(default=False, verbose_name='Is Role Specialst?'),
        ),
        migrations.AddField(
            model_name='middleeasternalliance',
            name='isFireSupport',
            field=models.BooleanField(default=False, verbose_name='Is Role Fire Support?'),
        ),
        migrations.AddField(
            model_name='middleeasternalliance',
            name='isLeadOrCommand',
            field=models.BooleanField(default=False, verbose_name='Is Role Lead or Command?'),
        ),
        migrations.AddField(
            model_name='middleeasternalliance',
            name='isSpecialst',
            field=models.BooleanField(default=False, verbose_name='Is Role Specialst?'),
        ),
        migrations.AddField(
            model_name='panasia',
            name='isFireSupport',
            field=models.BooleanField(default=False, verbose_name='Is Role Fire Support?'),
        ),
        migrations.AddField(
            model_name='panasia',
            name='isLeadOrCommand',
            field=models.BooleanField(default=False, verbose_name='Is Role Lead or Command?'),
        ),
        migrations.AddField(
            model_name='panasia',
            name='isSpecialst',
            field=models.BooleanField(default=False, verbose_name='Is Role Specialst?'),
        ),
        migrations.AddField(
            model_name='russiangroundforces',
            name='isFireSupport',
            field=models.BooleanField(default=False, verbose_name='Is Role Fire Support?'),
        ),
        migrations.AddField(
            model_name='russiangroundforces',
            name='isLeadOrCommand',
            field=models.BooleanField(default=False, verbose_name='Is Role Lead or Command?'),
        ),
        migrations.AddField(
            model_name='russiangroundforces',
            name='isSpecialst',
            field=models.BooleanField(default=False, verbose_name='Is Role Specialst?'),
        ),
        migrations.AddField(
            model_name='unitedstatesarmy',
            name='isFireSupport',
            field=models.BooleanField(default=False, verbose_name='Is Role Fire Support?'),
        ),
        migrations.AddField(
            model_name='unitedstatesarmy',
            name='isLeadOrCommand',
            field=models.BooleanField(default=False, verbose_name='Is Role Lead or Command?'),
        ),
        migrations.AddField(
            model_name='unitedstatesarmy',
            name='isSpecialst',
            field=models.BooleanField(default=False, verbose_name='Is Role Specialst?'),
        ),
        migrations.AddField(
            model_name='unitedstatesmarinecore',
            name='isFireSupport',
            field=models.BooleanField(default=False, verbose_name='Is Role Fire Support?'),
        ),
        migrations.AddField(
            model_name='unitedstatesmarinecore',
            name='isLeadOrCommand',
            field=models.BooleanField(default=False, verbose_name='Is Role Lead or Command?'),
        ),
        migrations.AddField(
            model_name='unitedstatesmarinecore',
            name='isSpecialst',
            field=models.BooleanField(default=False, verbose_name='Is Role Specialst?'),
        ),
    ]
