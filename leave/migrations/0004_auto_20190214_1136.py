# Generated by Django 2.1.5 on 2019-02-14 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0003_auto_20190204_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyleave',
            name='home_phone',
            field=models.CharField(max_length=20),
        ),
    ]
