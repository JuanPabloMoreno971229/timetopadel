# Generated by Django 4.2.2 on 2023-06-14 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torneo',
            name='hour',
            field=models.CharField(max_length=100, verbose_name='Hora de inicio'),
        ),
    ]