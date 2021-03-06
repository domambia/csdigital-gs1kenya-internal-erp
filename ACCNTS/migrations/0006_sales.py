# Generated by Django 2.1.5 on 2019-03-20 12:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0006_auto_20190319_0815'),
        ('ACCNTS', '0005_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.IntegerField(default=0)),
                ('payment_due', models.CharField(blank=True, max_length=200)),
                ('payment_terms', models.CharField(max_length=200)),
                ('date_of_sale', models.DateField(default=datetime.datetime.now)),
                ('invoice', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ACCNTS.Invoice')),
                ('member', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CRM.Client')),
            ],
        ),
    ]
