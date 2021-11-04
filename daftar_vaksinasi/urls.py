from django.urls import path
from .views import *

#app_name = 'forms'

urlpatterns = [ path('', index, name='index'),
                path('forms/tiket_vaksinasi', summary, name='tiket_vaksinasi'),
                path('forms/', form_peserta_vaksinasi, name='forms'),
]