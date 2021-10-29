import django_filters

from .models import SentraVaksinasi

class SentraFilter(django_filters.FilterSet):
    class Meta:
        model = SentraVaksinasi
        fields = '__all__'
        exclude = ['alamat',
                    'list_of_tanggal'
        ]