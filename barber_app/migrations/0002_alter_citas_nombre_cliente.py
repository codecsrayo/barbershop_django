# Generated by Django 4.0.4 on 2022-04-19 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citas',
            name='nombre_cliente',
            field=models.CharField(max_length=50),
        ),
    ]
