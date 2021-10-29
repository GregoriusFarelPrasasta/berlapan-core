from django.http import response
from django.shortcuts import render
from .models import SentraVaksinasi
from .filters import SentraFilter

# Create your views here.
def index(request):
    return render(request, 'index_daftar_vaksinasi.html')

def pilih_sentra_vaksinasi(request):
    list_of_sentra = SentraVaksinasi.objects.all()

    sentra_filter = SentraFilter(request.GET, queryset=list_of_sentra)
    list_of_sentra = sentra_filter.qs

    response = {'list_of_sentra' : list_of_sentra,
    'sentra_filter' : sentra_filter,
    }

    return render(request, 'pilih_sentra_vaksinasi.html', response)


def pilih_tanggal(request):
    list_of_sentra = SentraVaksinasi.objects.all()
    sentra_ditunjuk = list_of_sentra[0]

    tanggal_tersedia = sentra_ditunjuk.get_list_of_tanggal()

    response = {'tanggal_tersedia' : tanggal_tersedia,
                'sentra' : sentra_ditunjuk,
    }

    return render(request, 'pilih_tanggal.html', response)


def pilih_dosis(request):
    return render(request, 'pilih_dosis.html')

def summary(request):
    return render(request, 'tiket_vaksinasi.html')
    
