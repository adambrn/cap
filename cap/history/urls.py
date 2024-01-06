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
]

