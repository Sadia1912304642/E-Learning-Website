# Generated by Django 3.1.7 on 2021-05-10 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210503_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='Course',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Course',
        ),
        migrations.AddField(
            model_name='instructor',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Male'), (1, 'Female'), (-1, 'Others')], default=None),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Male'), (1, 'Female'), (-1, 'Others')], default=None),
        ),
    ]