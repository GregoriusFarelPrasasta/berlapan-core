from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [ path('', index, name='index'),
                path('tiket-vaksinasi', summary, name='summary'),
                path('pilih-sentra', pilih_sentra_vaksinasi, name='pilih_sentra_vaksinasi'),
                path('pilih-sentra/pilih-tanggal', pilih_tanggal, name='pilih_tanggal'),
                path('pilih-sentra/pilih-tanggal/pilih-dosis', pilih_dosis, name="pilih_dosis"),
              ]