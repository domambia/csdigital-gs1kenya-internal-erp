# Generated by Django 2.1.5 on 2019-04-17 12:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ACCNTS', '0017_auto_20190417_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='deduction',
            name='dated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]