# Generated by Django 2.1.5 on 2019-02-26 13:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20190215_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='alt_phone_number',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(14), django.core.validators.MinValueValidator(9)]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='kin_email',
            field=models.CharField(blank=True, max_length=100, unique=True, validators=[django.core.validators.EmailValidator('Enter a valid email address')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(14), django.core.validators.MinValueValidator(9)]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.Position', unique=True),
        ),
    ]
