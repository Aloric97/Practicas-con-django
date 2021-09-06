import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class orderFilter(django_filters.FilterSet):
    

    class Meta:
        model = order
        fields='costumer','product', 'status'