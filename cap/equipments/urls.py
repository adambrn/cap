from django.urls import path
from .views import *

app_name = 'equipments'

urlpatterns = [
    path('', EquipmentCatalogView.as_view(), name='equipments'),
    #компьютеры
    path('computer/list/', ComputersView.as_view(), name='computer_list'),
    path('computer/<int:pk>/', ComputerDetailView.as_view(), name='computer_detail'),
    path('computer/create/', ComputerCreateView.as_view(), name='computer_create'),
    path('computer/<int:pk>/update/', ComputerUpdateView.as_view(), name='computer_update'),
    path('computer/<int:pk>/delete/', ComputerDeleteView.as_view(), name='computer_delete'),
    #принтеры
    path('printer/list/', PrinterListView.as_view(), name='printer_list'),
    path('printer/<int:pk>/', PrinterDetailView.as_view(), name='printer_detail'),
    path('printer/create/', PrinterCreateView.as_view(), name='printer_create'),
    path('printer/<int:pk>/update/', PrinterUpdateView.as_view(), name='printer_update'),
    path('printer/<int:pk>/delete/', PrinterDeleteView.as_view(), name='printer_delete'),
    #мониторы
    path('monitor/list/', MonitorListView.as_view(), name='monitor_list'),
    path('monitor/<int:pk>/', MonitorDetailView.as_view(), name='monitor_detail'),
    path('monitor/create/', MonitorCreateView.as_view(), name='monitor_create'),
    path('monitor/<int:pk>/update/', MonitorUpdateView.as_view(), name='monitor_update'),
    path('monitor/<int:pk>/delete/', MonitorDeleteView.as_view(), name='monitor_delete'),
    #телефоны
    path('phone/list/', PhoneListView.as_view(), name='phone_list'),
    path('phone/<int:pk>/', PhoneDetailView.as_view(), name='phone_detail'),
    path('phone/create/', PhoneCreateView.as_view(), name='phone_create'),
    path('phone/<int:pk>/update/', PhoneUpdateView.as_view(), name='phone_update'),
    path('phone/<int:pk>/delete/', PhoneDeleteView.as_view(), name='phone_delete'),
    #сетевые
    path('network_device/list/', NetworkDeviceListView.as_view(), name='networkdevice_list'),
    path('network_device/<int:pk>/', NetworkDeviceDetailView.as_view(), name='networkdevice_detail'),
    path('network_device/create/', NetworkDeviceCreateView.as_view(), name='networkdevice_create'),
    path('network_device/<int:pk>/update/', NetworkDeviceUpdateView.as_view(), name='networkdevice_update'),
    path('network_device/<int:pk>/delete/', NetworkDeviceDeleteView.as_view(), name='networkdevice_delete'),
    #другое оборудование
    path('other_equipment/list/', OtherEquipmentListView.as_view(), name='otherequipment_list'),
    path('other_equipment/<int:pk>/', OtherEquipmentDetailView.as_view(), name='otherequipment_detail'),
    path('other_equipment/create/', OtherEquipmentCreateView.as_view(), name='otherequipment_create'),
    path('other_equipment/<int:pk>/update/', OtherEquipmentUpdateView.as_view(), name='otherequipment_update'),
    path('other_equipment/<int:pk>/delete/', OtherEquipmentDeleteView.as_view(), name='otherequipment_delete'),
    ]
