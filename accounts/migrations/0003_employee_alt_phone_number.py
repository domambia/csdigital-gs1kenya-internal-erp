# Generated by Django 2.1.5 on 2019-01-28 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190125_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='alt_phone_number',
            field=models.IntegerField(default=0),
        ),
    ]