from django_filters.views import FilterView
from .filters import *
from cap.mixins import *
from .tables import *
from components.tables import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, ListView, DeleteView, UpdateView
from django_tables2 import MultiTableMixin, SingleTableMixin, SingleTableView
from django.views.generic.base import TemplateView
from view_breadcrumbs import DetailBreadcrumbMixin, BaseBreadcrumbMixin, CreateBreadcrumbMixin, DeleteBreadcrumbMixin, UpdateBreadcrumbMixin
from view_breadcrumbs.generic.base import BaseModelBreadcrumbMixin
from django.utils.functional import cached_property
from django.views.generic import DetailView

class EquipmentCatalogView(BaseBreadcrumbMixin, BaseContextMixin, LoginRequiredMixin, MultiTableMixin, TemplateView):
    
    template_name = 'equipments/equipments.html'
    def get_tables(self):
        tables = [
            ComputerTable(Computer.objects.all()),
            PrinterTable(Printer.objects.all()),
            PhoneTable(Phone.objects.all()),
            NetworkDeviceTable(NetworkDevice.objects.all()),
            OtherEquipmentTable(OtherEquipment.objects.all()),
        ]
        return tables
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] =  [
            {'title': 'Компьютеры', 'url': 'equipments:computer_list'},
            {'title': 'Принтеры', 'url': 'equipments:printer_list'},
            {'title': 'Сетевые устройства', 'url': 'equipments:network_device_list'},
            {'title': 'Телефоны', 'url': 'equipments:phone_list'},
            {'title': 'Другие устройства', 'url': 'equipments:other_equipment_list'},
            ]
     
        return context
    
    @cached_property
    def crumbs(self):
        return [("Обрудование", "/")]

#Базовые классы оборудования
class EquipmentView(BaseModelBreadcrumbMixin, BaseContextMixin, LoginRequiredMixin, SingleTableMixin, FilterView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] =  [
            {'title': 'Компьютеры', 'url': 'equipments:computer_list'},
            {'title': 'Принтеры', 'url': 'equipments:printer_list'},
            {'title': 'Сетевые устройства', 'url': 'equipments:network_device_list'},
            {'title': 'Телефоны', 'url': 'equipments:phone_list'},
            {'title': 'Другие устройства', 'url': 'equipments:other_equipment_list'},
            ]
     
        return context
    
    @cached_property
    def crumbs(self):
        return [("Обрудование", "/"), (self.model_name_title_plural, "/")]

class EquipmentDetailView(DetailBreadcrumbMixin, BaseContextMixin, LoginRequiredMixin, DetailView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] =  [
            {'title': 'Компьютеры', 'url': 'equipments:computer_list'},
            {'title': 'Принтеры', 'url': 'equipments:printer_list'},
            {'title': 'Сетевые устройства', 'url': 'equipments:network_device_list'},
            {'title': 'Телефоны', 'url': 'equipments:phone_list'},
            {'title': 'Другие устройства', 'url': 'equipments:other_equipment_list'},
            ]
     
        return context

#Компьютеры
class ComputersView(EquipmentView):
    model = Computer
    template_name = 'equipments/computers.html'
    table_class = ComputerTable
    filterset_class = ComputerFilter

class ComputerDetailView(MultiTableMixin,EquipmentDetailView):
    
    model = Computer
    template_name = 'equipments/computer_detail.html'

    def get_tables(self):
        computer_id = self.kwargs.get('pk')
        computer = Computer.objects.get(pk=computer_id)
        print(computer)
        tables = [
            ProcessorTable(Processor.objects.filter(in_computer=computer)),
            RAMTable(RAM.objects.filter(in_computer=computer)),
            MotherboardTable(Motherboard.objects.filter(in_computer=computer)),
            GraphicsCardTable(GraphicsCard.objects.filter(in_computer=computer)),
            StorageTable(Storage.objects.filter(in_computer=computer)), 
            PowerSupplyTable(PowerSupply.objects.filter(in_computer=computer)),
            CoolerTable(Cooler.objects.filter(in_computer=computer)),
            CaseTable(Case.objects.filter(in_computer=computer)),
            NetworkCardTable(NetworkCard.objects.filter(in_computer=computer)), 
        ]
        return tables


#Принтеры
class PrintersView(EquipmentView):
    model = Printer
    template_name = 'equipments/computers.html'
    table_class = PrinterTable
    filterset_class = ComputerFilter  

class PrinterDetailView(EquipmentDetailView):
    
    model = Printer
    template_name = 'equipments/printer_detail.html'

#Сетевое оборудование
class NetworkDeviceView(EquipmentView):
    model = NetworkDevice
    template_name = 'equipments/network_device.html'
    table_class = NetworkDeviceTable
    filterset_class = ComputerFilter

class NetworkDeviceDetailView(EquipmentDetailView): 
    model = NetworkDevice
    template_name = 'equipments/network_device_detail.html'

#Телефоны
class PhoneView(EquipmentView):
    model = Phone
    template_name = 'equipments/phone.html'
    table_class = PhoneTable
    filterset_class = ComputerFilter

class PhoneDetailView(EquipmentDetailView): 
    model = Phone
    template_name = 'equipments/phone_detail.html'

#Другое оборудование
class OtherEquipmentView(EquipmentView):
    model = OtherEquipment
    template_name = 'equipments/other_equipment.html'
    table_class = OtherEquipmentTable
    filterset_class = ComputerFilter

class OtherEquipmentDetailView(EquipmentDetailView): 
    model = OtherEquipment
    template_name = 'equipments/other_equipment_detail.html'


