# Generated by Django 2.1 on 2019-08-01 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentCon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_nu', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('country', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Student_info',
            },
        ),
    ]
