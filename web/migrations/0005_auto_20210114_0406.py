# Generated by Django 3.1.5 on 2021-01-14 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20210114_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitacion',
            name='imagen',
            field=models.URLField(),
        ),
    ]
