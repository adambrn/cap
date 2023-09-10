from django_filters.views import FilterView
from .filters import *
from cap.mixins import *
from .tables import *
from components.tables import *
from .models import *
from equipments.forms import *
from django.views.generic import DetailView, CreateView, ListView, DeleteView, UpdateView
from django_tables2 import MultiTableMixin, SingleTableMixin, SingleTableView
from django.views.generic.base import TemplateView
from view_breadcrumbs import DetailBreadcrumbMixin, BaseBreadcrumbMixin, CreateBreadcrumbMixin, DeleteBreadcrumbMixin, UpdateBreadcrumbMixin
from view_breadcrumbs.generic.base import BaseModelBreadcrumbMixin
from django.utils.functional import cached_property
from django.views.generic import DetailView

class EquipmentCatalogView(BaseBreadcrumbMixin, BaseEquipmentMixin, MultiTableMixin, TemplateView):
    
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
    
    
    @cached_property
    def crumbs(self):
        return [("Обрудование", "/")]

#Базовые классы оборудования
class BaseEquipmentListView(BaseModelBreadcrumbMixin, BaseEquipmentMixin, SingleTableMixin, FilterView):
    
    @cached_property
    def crumbs(self):
        return [("Обрудование", "/"), (self.model_name_title_plural, "/")]

class BaseEquipmentDetailView(DetailBreadcrumbMixin, BaseEquipmentMixin, DetailView):
    pass

class BaseEquipmentDeleteView(DeleteBreadcrumbMixin, BaseEquipmentMixin, DeleteView):
    pass

class BaseEquipmentUpdateView(UpdateBreadcrumbMixin, BaseEquipmentMixin, UpdateView):
    def get_context_data(self, **kwargs):
        """Add the models verbose name to the context dictionary."""

        kwargs.update({
            "model_verbose_name": self.form_class._meta.model._meta.verbose_name,})
        return super().get_context_data(**kwargs)

class BaseEquipmentCreateView(CreateBreadcrumbMixin, BaseEquipmentMixin, CreateView):
    def get_context_data(self, **kwargs):
        """Add the models verbose name to the context dictionary."""

        kwargs.update({
            "model_verbose_name": self.form_class._meta.model._meta.verbose_name,})
        return super().get_context_data(**kwargs)

#Компьютеры
class ComputersView(BaseEquipmentListView):
    model = Computer
    template_name = 'equipments/computers.html'
    table_class = ComputerTable
    filterset_class = ComputerFilter

class ComputerDetailView(MultiTableMixin, BaseEquipmentDetailView):
    
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

class ComputerCreateView(BaseEquipmentCreateView):
    model = Computer
    form_class = ComputerForm
    template_name = 'equipments/computer_create.html'

#Принтеры
class PrintersView(BaseEquipmentListView):
    model = Printer
    template_name = 'equipments/computers.html'
    table_class = PrinterTable
    filterset_class = ComputerFilter  

class PrinterDetailView(BaseEquipmentDetailView):
    
    model = Printer
    template_name = 'equipments/printer_detail.html'

#Сетевое оборудование
class NetworkDeviceView(BaseEquipmentListView):
    model = NetworkDevice
    template_name = 'equipments/network_device.html'
    table_class = NetworkDeviceTable
    filterset_class = ComputerFilter

class NetworkDeviceDetailView(BaseEquipmentDetailView): 
    model = NetworkDevice
    template_name = 'equipments/network_device_detail.html'

#Телефоны
class PhoneView(BaseEquipmentListView):
    model = Phone
    template_name = 'equipments/phone.html'
    table_class = PhoneTable
    filterset_class = ComputerFilter

class PhoneDetailView(BaseEquipmentDetailView): 
    model = Phone
    template_name = 'equipments/phone_detail.html'

#Другое оборудование
class OtherEquipmentView(BaseEquipmentListView):
    model = OtherEquipment
    template_name = 'equipments/other_equipment.html'
    table_class = OtherEquipmentTable
    filterset_class = ComputerFilter

class OtherEquipmentDetailView(BaseEquipmentDetailView): 
    model = OtherEquipment
    template_name = 'equipments/other_equipment_detail.html'


