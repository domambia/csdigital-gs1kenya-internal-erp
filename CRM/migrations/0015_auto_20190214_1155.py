# Generated by Django 2.1.5 on 2019-02-14 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0014_auto_20190210_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='category',
            field=models.CharField(choices=[('Category a', 'Category A'), ('Category b', 'Category B'), ('Category b', 'Category B'), ('Category c', 'Category C'), ('Category d', 'Category D'), ('Category e', 'Category E')], default='No category', max_length=80),
        ),
        migrations.AlterField(
            model_name='client',
            name='sector',
            field=models.CharField(choices=[('Academia', 'Academia'), ('Agribusiness', 'Agribusiness'), ('Helathcare', 'Helathcare'), ('Manufacturer,trading &financial institutions', 'Manufacturer,Trading &Financial Institutions'), ('Retailer', 'Retailer'), ('Transport / communication', 'Transport / Communication'), ('Supply  chain,warehousing  & construction', 'Supply  Chain,warehousing  & construction')], default='No sector', max_length=200),
        ),
    ]
