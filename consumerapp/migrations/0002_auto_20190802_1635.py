# Generated by Django 2.1 on 2019-08-02 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumerapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcon',
            name='password',
            field=models.CharField(default='None', max_length=55),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentcon',
            name='country',
            field=models.CharField(default='Seychelles', max_length=50),
        ),
        migrations.AlterField(
            model_name='studentcon',
            name='dob',
            field=models.DateField(default='2005-12-10'),
        ),
        migrations.AlterField(
            model_name='studentcon',
            name='first_name',
            field=models.CharField(default='Kayla', max_length=50),
        ),
        migrations.AlterField(
            model_name='studentcon',
            name='last_name',
            field=models.CharField(default='Christian', max_length=50),
        ),
        migrations.AlterField(
            model_name='studentcon',
            name='phone_nu',
            field=models.CharField(default='8023141834', max_length=50),
        ),
    ]