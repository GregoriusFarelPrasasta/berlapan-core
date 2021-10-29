from django.contrib import admin

from daftar_vaksinasi.models import *

# Register your models here.
admin.site.register(SentraVaksinasi)
admin.site.register(TanggalTersedia)
admin.site.register(JamTersedia)