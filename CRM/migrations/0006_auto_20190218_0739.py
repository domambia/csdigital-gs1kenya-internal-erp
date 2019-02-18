# Generated by Django 2.1.5 on 2019-02-18 07:39

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0005_barcode_feedback_supplier_training'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='all_trainee',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'BrugKe'), (2, 'gs1')], default='1,2', max_length=3),
        ),
    ]
