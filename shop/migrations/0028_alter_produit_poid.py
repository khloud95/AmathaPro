# Generated by Django 3.2.8 on 2021-10-20 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_alter_atelier_prix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='poid',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
    ]
