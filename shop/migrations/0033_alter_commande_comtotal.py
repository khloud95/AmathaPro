# Generated by Django 3.2.8 on 2021-10-22 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0032_alter_commande_compoidsfinal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='comTotal',
            field=models.IntegerField(),
        ),
    ]