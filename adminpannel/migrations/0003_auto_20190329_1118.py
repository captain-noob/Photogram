# Generated by Django 2.1.5 on 2019-03-29 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpannel', '0002_auto_20190329_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='phone',
            field=models.BigIntegerField(unique=True),
        ),
    ]
