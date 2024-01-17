from django_filters import FilterSet, CharFilter
from django.db.models import Q

class CatalogsFilter(FilterSet):
    global_search = CharFilter(method='search', label='Поиск')

    def search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) 
        )


