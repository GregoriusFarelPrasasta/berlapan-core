# Generated by Django 3.2.8 on 2021-10-27 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daftar_vaksinasi', '0002_jamtersedia_tanggaltersedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jamtersedia',
            name='jam',
            field=models.CharField(max_length=10),
        ),
    ]
