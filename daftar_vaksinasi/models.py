from django.db import models

# Create your models here.
class JamTersedia(models.Model):
    jam = models.CharField(max_length=20)

class TanggalTersedia(models.Model):
    tanggal = models.DateField()
    list_of_jam_tersedia = models.ManyToManyField(JamTersedia)

    def get_jam_tersedia(self):
        return (self.list_of_jam_tersedia.all())

class SentraVaksinasi(models.Model):
    provinsi = models.CharField(max_length=50)
    kabupaten_kota = models.CharField(max_length=50)
    alamat = models.TextField()
    list_of_tanggal = models.ManyToManyField(TanggalTersedia)

    def get_list_of_tanggal(self):
        return(self.list_of_tanggal.all())



