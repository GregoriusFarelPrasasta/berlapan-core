# Generated by Django 3.2.8 on 2021-11-03 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daftar_vaksinasi', '0006_auto_20211103_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provinsi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provinsi', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='pesertavaksinasi',
            name='jam_vaksinasi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='daftar_vaksinasi.jamtersedia'),
        ),
        migrations.AlterField(
            model_name='pesertavaksinasi',
            name='sentra_vaksinasi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='daftar_vaksinasi.sentravaksinasi'),
        ),
        migrations.AlterField(
            model_name='pesertavaksinasi',
            name='tanggal_vaksinasi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='daftar_vaksinasi.tanggaltersedia'),
        ),
        migrations.CreateModel(
            name='KabupatenKota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kabupaten_kota', models.CharField(max_length=100)),
                ('provinsi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='daftar_vaksinasi.provinsi')),
            ],
        ),
        migrations.AddField(
            model_name='pesertavaksinasi',
            name='kabupaten_kota',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='daftar_vaksinasi.kabupatenkota'),
        ),
        migrations.AddField(
            model_name='pesertavaksinasi',
            name='provinsi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='daftar_vaksinasi.provinsi'),
        ),
        migrations.AlterField(
            model_name='sentravaksinasi',
            name='kabupaten_kota',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='daftar_vaksinasi.kabupatenkota'),
        ),
        migrations.AlterField(
            model_name='sentravaksinasi',
            name='provinsi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='daftar_vaksinasi.provinsi'),
        ),
    ]
