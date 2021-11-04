from django.contrib import admin

from daftar_vaksinasi.models import *

# Register your models here.
admin.site.register(SentraVaksinasi)
admin.site.register(JamTersedia)
admin.site.register(TanggalTersedia)
admin.site.register(Provinsi)
admin.site.register(KabupatenKota)
admin.site.register(PesertaVaksinasi)

