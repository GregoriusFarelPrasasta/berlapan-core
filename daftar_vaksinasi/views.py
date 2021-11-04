
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .forms import DaftarVaksinasiForm

# Create your views here.
def index(request):
    return render(request, 'index_daftar_vaksinasi.html')


def summary(request):
    list_of_peserta = PesertaVaksinasi.objects.all()

    result = PesertaVaksinasi
    for peserta in list_of_peserta:
        if peserta.nama == 'Greg':
            result = peserta

    response = {'result':result}
    return render(request, 'tiket_vaksinasi.html', response)


def form_peserta_vaksinasi(request):
    peserta_vaksinasi_form = DaftarVaksinasiForm(request.POST or None)
    if peserta_vaksinasi_form.is_valid():
        peserta_vaksinasi_form.save()
        

    response = {'peserta_vaksinasi_form' : peserta_vaksinasi_form}
    return render(request, 'forms.html', response)


