from django_filters import FilterSet, CharFilter
from django.db.models import Q

class HistoryFilter(FilterSet):
    global_search = CharFilter(method='search', label='Поиск')

    def search(self, queryset, name, value):
        return queryset.filter(
            Q(location__name__icontains=value) |
            Q(employee__name__icontains=value) |
            Q(start_date__icontains=value) |
            Q(end_date__icontains=value) 
        )


