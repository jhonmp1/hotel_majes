# Generated by Django 3.1.5 on 2021-01-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_habitacion_contra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habitacion',
            name='contra',
        ),
        migrations.AddField(
            model_name='reserva',
            name='contra',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
