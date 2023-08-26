from django_filters import FilterSet, CharFilter
from django.db.models import Q
from .models import Computer

class ComputerFilter(FilterSet):
    global_search = CharFilter(method='search', label='Поиск')

    def search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) | Q(serial_number__icontains=value) | 
            Q(manufacturer__name__icontains=value)
        )
