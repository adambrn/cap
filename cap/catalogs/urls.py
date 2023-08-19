from django.urls import path
from .views import ComponentListView, CreateComponentView, EquipmentCatalogView, ComputerComponentsView, ComponentDetailView, SelectComponentView

from django.conf.urls.static import static
from django.conf import settings

app_name = 'catalogs'

urlpatterns = [
    path('', EquipmentCatalogView.as_view(), name='equipment_catalog'),
    path('equipment/<int:pk>/components/', ComputerComponentsView.as_view(), name='equipment_components'),
    path('components/', ComponentListView.as_view(), name='components'),
    path('components/<str:model>/<int:pk>/', ComponentDetailView.as_view(), name='component_detail'),
    path('components/create/<str:component_type>/', CreateComponentView.as_view(), name='create-component'),
    path('components/create/', SelectComponentView.as_view(), name='select-component'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)