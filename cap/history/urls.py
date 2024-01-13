from django.urls import path
from history.views import *

app_name = 'history'

urlpatterns = [
    path('', HistoryView.as_view(), name='history'),
    path('computers/', AllComputerHistoryListView.as_view(), name='all_computer_history_list'),
    path('computer/<int:equipment_pk>', ComputerHistoryListView.as_view(), name='computer_history_list'),
    path('computer/<int:equipment_pk>/employee_update/<int:pk>', EmployeeComputerHistoryUpdateView.as_view(), name='computer_history_employee_update'),
    path('computer/<int:equipment_pk>/employee_create', EmployeeComputerHistoryCreateView.as_view(), name='computer_history_employee_create'),
    path('computer/<int:equipment_pk>/location_update/<int:pk>', LocationComputerHistoryUpdateView.as_view(), name='computer_history_location_update'),
    path('computer/<int:equipment_pk>/location_create', LocationComputerHistoryCreateView.as_view(), name='computer_history_location_create'),
    path('computer/<int:equipment_pk>/location_clear/<int:pk>', LocationComputerHistoryClearView.as_view(), name='computer_history_location_clear'),
    path('computer/<int:equipment_pk>/employee_clear/<int:pk>', EmployeeComputerHistoryClearView.as_view(), name='computer_history_employee_clear'),
    #принтер
    path('printers/', AllPrinterHistoryListView.as_view(), name='all_printer_history_list'),
    path('printer/<int:equipment_pk>', PrinterHistoryListView.as_view(), name='printer_history_list'),
    path('printer/<int:equipment_pk>/employee_update/<int:pk>', EmployeePrinterHistoryUpdateView.as_view(), name='printer_history_employee_update'),
    path('printer/<int:equipment_pk>/employee_create', EmployeePrinterHistoryCreateView.as_view(), name='printer_history_employee_create'),
    path('printer/<int:equipment_pk>/location_update/<int:pk>', LocationPrinterHistoryUpdateView.as_view(), name='printer_history_location_update'),
    path('printer/<int:equipment_pk>/location_create', LocationPrinterHistoryCreateView.as_view(), name='printer_history_location_create'),
    path('printer/<int:equipment_pk>/location_clear/<int:pk>', LocationPrinterHistoryClearView.as_view(), name='printer_history_location_clear'),
    path('printer/<int:equipment_pk>/employee_clear/<int:pk>', EmployeePrinterHistoryClearView.as_view(), name='printer_history_employee_clear'),
    #монитор
    path('monitors/', AllMonitorHistoryListView.as_view(), name='all_monitor_history_list'),
    path('monitor/<int:equipment_pk>', MonitorHistoryListView.as_view(), name='monitor_history_list'),
    path('monitor/<int:equipment_pk>/employee_update/<int:pk>', EmployeeMonitorHistoryUpdateView.as_view(), name='monitor_history_employee_update'),
    path('monitor/<int:equipment_pk>/employee_create', EmployeeMonitorHistoryCreateView.as_view(), name='monitor_history_employee_create'),
    path('monitor/<int:equipment_pk>/location_update/<int:pk>', LocationMonitorHistoryUpdateView.as_view(), name='monitor_history_location_update'),
    path('monitor/<int:equipment_pk>/location_create', LocationMonitorHistoryCreateView.as_view(), name='monitor_history_location_create'),
    path('monitor/<int:equipment_pk>/location_clear/<int:pk>', LocationMonitorHistoryClearView.as_view(), name='monitor_history_location_clear'),
    path('monitor/<int:equipment_pk>/employee_clear/<int:pk>', EmployeeMonitorHistoryClearView.as_view(), name='monitor_history_employee_clear'),
    #телефоны
    path('phones/', AllPhoneHistoryListView.as_view(), name='all_phone_history_list'),
    path('phone/<int:equipment_pk>', PhoneHistoryListView.as_view(), name='phone_history_list'),
    path('phone/<int:equipment_pk>/employee_update/<int:pk>', EmployeePhoneHistoryUpdateView.as_view(), name='phone_history_employee_update'),
    path('phone/<int:equipment_pk>/employee_create', EmployeePhoneHistoryCreateView.as_view(), name='phone_history_employee_create'),
    path('phone/<int:equipment_pk>/location_update/<int:pk>', LocationPhoneHistoryUpdateView.as_view(), name='phone_history_location_update'),
    path('phone/<int:equipment_pk>/location_create', LocationPhoneHistoryCreateView.as_view(), name='phone_history_location_create'),
    path('phone/<int:equipment_pk>/location_clear/<int:pk>', LocationPhoneHistoryClearView.as_view(), name='phone_history_location_clear'),
    path('phone/<int:equipment_pk>/employee_clear/<int:pk>', EmployeePhoneHistoryClearView.as_view(), name='phone_history_employee_clear'),
    #сетевое
    path('networkdevices/', AllNetworkDeviceHistoryListView.as_view(), name='all_networkdevice_history_list'),
    path('networkdevice/<int:equipment_pk>', NetworkDeviceHistoryListView.as_view(), name='networkdevice_history_list'),
    path('networkdevice/<int:equipment_pk>/employee_update/<int:pk>', EmployeeNetworkDeviceHistoryUpdateView.as_view(), name='networkdevice_history_employee_update'),
    path('networkdevice/<int:equipment_pk>/employee_create', EmployeeNetworkDeviceHistoryCreateView.as_view(), name='networkdevice_history_employee_create'),
    path('networkdevice/<int:equipment_pk>/location_update/<int:pk>', LocationNetworkDeviceHistoryUpdateView.as_view(), name='networkdevice_history_location_update'),
    path('networkdevice/<int:equipment_pk>/location_create', LocationNetworkDeviceHistoryCreateView.as_view(), name='networkdevice_history_location_create'),
    path('networkdevice/<int:equipment_pk>/location_clear/<int:pk>', LocationNetworkDeviceHistoryClearView.as_view(), name='networkdevice_history_location_clear'),
    path('networkdevice/<int:equipment_pk>/employee_clear/<int:pk>', EmployeeNetworkDeviceHistoryClearView.as_view(), name='networkdevice_history_employee_clear'),
    #другое
    path('otherequipments/', AllOtherEquipmentHistoryListView.as_view(), name='all_otherequipment_history_list'),
    path('otherequipment/<int:equipment_pk>', OtherEquipmentHistoryListView.as_view(), name='otherequipment_history_list'),
    path('otherequipment/<int:equipment_pk>/employee_update/<int:pk>', EmployeeOtherEquipmentHistoryUpdateView.as_view(), name='otherequipment_history_employee_update'),
    path('otherequipment/<int:equipment_pk>/employee_create', EmployeeOtherEquipmentHistoryCreateView.as_view(), name='otherequipment_history_employee_create'),
    path('otherequipment/<int:equipment_pk>/location_update/<int:pk>', LocationOtherEquipmentHistoryUpdateView.as_view(), name='otherequipment_history_location_update'),
    path('otherequipment/<int:equipment_pk>/location_create', LocationOtherEquipmentHistoryCreateView.as_view(), name='otherequipment_history_location_create'),
    path('otherequipment/<int:equipment_pk>/location_clear/<int:pk>', LocationOtherEquipmentHistoryClearView.as_view(), name='otherequipment_history_location_clear'),
    path('otherequipment/<int:equipment_pk>/employee_clear/<int:pk>', EmployeeOtherEquipmentHistoryClearView.as_view(), name='otherequipment_history_employee_clear'),

    # компоненты
    path('component/<str:component>/<int:pk>', ComponentHistoryListView.as_view(), name='component_history_list'),
]

