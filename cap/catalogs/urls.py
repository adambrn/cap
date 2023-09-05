from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'catalogs'

urlpatterns = [
    path('', EquipmentCatalogView.as_view(), name='equipments'),
    path('computers/', ComputersView.as_view(), name='computer_list'),
    path('computers/<int:pk>', ComputerDetailView.as_view(), name='computer_detail'),
    #path('computers/<int:pk>/components/', ComputerComponentsView.as_view(), name='computers_components'),
    path('components/', ComponentListView.as_view(), name='components'),
    #path('components/<str:model>/<int:pk>/', ComponentDetailView.as_view(), name='component_detail'),
    #path('components/create/<str:component_type>/', CreateComponentView.as_view(), name='create_component'),
    
    path('components/create/', SelectComponentView.as_view(), name='select_component'),
    
    path('components/processor_list/', ProcessorListView.as_view(), name='processor_list'), 
    path('components/processor/create', ProcessorCreateView.as_view(), name='processor_create'),
    path('components/processor/<int:pk>/update', ProcessorUpdateView.as_view(), name='processor_update'),
    path('components/processor/<int:pk>/delete', ProcessorDeleteView.as_view(), name='processor_delete'),
    path('components/processor/<int:pk>/detail', ProcessorDetailView.as_view(), name='processor_detail'), 
    
    path('components/motherboard_list/', MotherboardListView.as_view(), name='motherboard_list'),
    path('components/motherboard_detail/<int:pk>/', MotherboardDetailView.as_view(), name='motherboard_detail'),

    path('components/ram_list/', RAMListView.as_view(), name='ram_list'),
    path('components/ram_detail/<int:pk>/', RAMDetailView.as_view(), name='ram_detail'),

    path('components/graphicscard_list/', GraphicsCardListView.as_view(), name='graphicscard_list'),  
    path('components/graphicscard_detail/<int:pk>/', GraphicsCardDetailView.as_view(), name='graphicscard_detail'),

    path('components/storage_list/', StorageListView.as_view(), name='storage_list'),
    path('components/storage_detail/<int:pk>/', StorageDetailView.as_view(), name='storage_detail'),   

    path('components/powersupply_list/', PowerSupplyListView.as_view(), name='powersupply_list'),
    path('components/powersupply_detail/<int:pk>/', PowerSupplyDetailView.as_view(), name='powersupply_detail'),

    path('components/cooler_list/', CoolerListView.as_view(), name='cooler_list'),
    path('components/cooler_detail/<int:pk>/', CoolerDetailView.as_view(), name='cooler_detail'),

    path('components/case_list/', CaseListView.as_view(), name='case_list'),
    path('components/case_detail/<int:pk>/', CaseDetailView.as_view(), name='case_detail'),

    path('components/networkcard_list/', NetworkCardListView.as_view(), name='networkcard_list'),
    path('components/networkcard_detail/<int:pk>/', NetworkCardDetailView.as_view(), name='networkcard_detail'),
    #path('components/processor_detail/<int:pk>/', ProcessorDetailView.as_view(), name='processor_detail'), 
    path('printers/', PrintersView.as_view(), name='printer_list'),
    path('printers/<int:pk>', PrinterDetailView.as_view(), name='printer_detail'),
    path('network_device/', NetworkDeviceView.as_view(), name='network_device_list'),
    path('network_device/<int:pk>', NetworkDeviceDetailView.as_view(), name='network_device_detail'),
    path('phone/', PhoneView.as_view(), name='phone_list'),
    path('phone/<int:pk>', PhoneDetailView.as_view(), name='phone_detail'),
    path('other_equipment/', OtherEquipmentView.as_view(), name='other_equipment_list'),
    path('other_equipment/<int:pk>', OtherEquipmentDetailView.as_view(), name='other_equipment_detail'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)