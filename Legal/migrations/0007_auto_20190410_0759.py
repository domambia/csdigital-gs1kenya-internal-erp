# Generated by Django 2.1.5 on 2019-04-10 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Legal', '0006_auto_20190409_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contract',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='gs1docs',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='letter',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]