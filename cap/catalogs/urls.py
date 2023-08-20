from django.urls import path
from .views import (ComponentListView, 
                    CreateComponentView, 
                    EquipmentCatalogView, 
                    ComputerComponentsView, 
                    ComponentDetailView, PrinterDetailView, PrintersView, 
                    RamListView, 
                    SelectComponentView,
                    ComputersView,
                    ComputerDetailView,
                    )

from django.conf.urls.static import static
from django.conf import settings

app_name = 'catalogs'

urlpatterns = [
    path('', EquipmentCatalogView.as_view(), name='index'),
    path('computers/', ComputersView.as_view(), name='computer_list'),
    path('computers/<int:pk>', ComputerDetailView.as_view(), name='computer_detail'),
    path('computers/<int:pk>/components/', ComputerComponentsView.as_view(), name='computers_components'),
    path('components/', ComponentListView.as_view(), name='components'),
    path('components/<str:model>/<int:pk>/', ComponentDetailView.as_view(), name='component_detail'),
    path('components/create/<str:component_type>/', CreateComponentView.as_view(), name='create_component'),
    path('components/create/', SelectComponentView.as_view(), name='select_component'),
    path('components/ram_list/', RamListView.as_view(), name='ram_list'), 
    path('components/ram_detail/<int:pk>/', ComponentDetailView.as_view(), name='ram_detail'), 
    path('printers/', PrintersView.as_view(), name='printer_list'),
    path('printers/<int:pk>', PrinterDetailView.as_view(), name='printer_detail'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)