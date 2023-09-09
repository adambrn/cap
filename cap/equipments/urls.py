from django.urls import path
from .views import *

app_name = 'equipments'

urlpatterns = [
    path('', EquipmentCatalogView.as_view(), name='equipments'),
    path('computers/', ComputersView.as_view(), name='computer_list'),
    path('computers/<int:pk>', ComputerDetailView.as_view(), name='computer_detail'),
    
    path('printers/', PrintersView.as_view(), name='printer_list'),
    path('printers/<int:pk>', PrinterDetailView.as_view(), name='printer_detail'),
    path('network_device/', NetworkDeviceView.as_view(), name='network_device_list'),
    path('network_device/<int:pk>', NetworkDeviceDetailView.as_view(), name='network_device_detail'),
    path('phone/', PhoneView.as_view(), name='phone_list'),
    path('phone/<int:pk>', PhoneDetailView.as_view(), name='phone_detail'),
    path('other_equipment/', OtherEquipmentView.as_view(), name='other_equipment_list'),
    path('other_equipment/<int:pk>', OtherEquipmentDetailView.as_view(), name='other_equipment_detail'),
    ]
