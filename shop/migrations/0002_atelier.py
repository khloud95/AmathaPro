# Generated by Django 3.2.7 on 2021-09-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atelier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=150)),
                ('nbrPersonneMax', models.IntegerField()),
                ('dateDebut', models.DateField()),
                ('heureDebut', models.TimeField()),
                ('heureFin', models.TimeField()),
                ('adresse', models.CharField(max_length=150)),
                ('prix', models.IntegerField()),
            ],
        ),
    ]
