# Generated by Django 2.1.5 on 2019-01-25 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0003_auto_20190125_1049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='trainer',
            new_name='client_name',
        ),
    ]