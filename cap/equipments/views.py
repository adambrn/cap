from django.utils import timezone
from django.urls import reverse_lazy
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
from django.db.models import Max

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
    template_name = 'equipments/computer_list.html'
    table_class = ComputerTable
    filterset_class = ComputerFilter

class ComputerDetailView(MultiTableMixin, BaseEquipmentDetailView):
    model = Computer
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получаем текущую дату и время
        current_date = timezone.now()

        # Получаем последнюю запись истории для данного компьютера на текущую дату
        last_history_entry = self.object.computerhistory_set.filter(
            computer=self.object, start_date__lte=current_date
        ).aggregate(Max('start_date'))

        if last_history_entry['start_date__max']:
            last_history_entry = self.object.computerhistory_set.filter(
                computer=self.object, start_date=last_history_entry['start_date__max']
            ).last()
            context['current_history'] = last_history_entry
        return context
    
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

class ComputerUpdateView(BaseEquipmentUpdateView):
    model = Computer
    form_class = ComputerForm

class ComputerDeleteView(BaseEquipmentDeleteView):
    model = Computer
    success_url = reverse_lazy('equipments:computer_list')

#Принтеры
class PrinterListView(BaseEquipmentListView):
    model = Printer
    template_name = 'equipments/printer_list.html'
    table_class = PrinterTable
    filterset_class = ComputerFilter  

class PrinterDetailView(BaseEquipmentDetailView):
    model = Printer

class PrinterCreateView(BaseEquipmentCreateView):
    model = Printer
    form_class = PrinterForm

class PrinterUpdateView(BaseEquipmentUpdateView):
    model = Printer
    form_class = PrinterForm

class PrinterDeleteView(BaseEquipmentDeleteView):
    model = Printer
    success_url = reverse_lazy('equipments:printer_list')
#Сетевое оборудование
class NetworkDeviceListView(BaseEquipmentListView):
    model = NetworkDevice
    template_name = 'equipments/networkdevice_list.html'
    table_class = NetworkDeviceTable
    filterset_class = ComputerFilter  

class NetworkDeviceDetailView(BaseEquipmentDetailView):
    model = NetworkDevice

class NetworkDeviceCreateView(BaseEquipmentCreateView):
    model = NetworkDevice
    form_class = NetworkDeviceForm

class NetworkDeviceUpdateView(BaseEquipmentUpdateView):
    model = NetworkDevice
    form_class = NetworkDeviceForm

class NetworkDeviceDeleteView(BaseEquipmentDeleteView):
    model = NetworkDevice
    success_url = reverse_lazy('equipments:networkdevice_list')

#Телефоны
class PhoneListView(BaseEquipmentListView):
    model = Phone
    template_name = 'equipments/phone_list.html'
    table_class = PhoneTable
    filterset_class = ComputerFilter

class PhoneDetailView(BaseEquipmentDetailView): 
    model = Phone

class PhoneCreateView(BaseEquipmentCreateView):
    model = Phone
    form_class = PhoneForm

class PhoneUpdateView(BaseEquipmentUpdateView):
    model = Phone
    form_class = PhoneForm

class PhoneDeleteView(BaseEquipmentDeleteView):
    model = Phone
    success_url = reverse_lazy('equipments:phone_list')


#Другое оборудование
class OtherEquipmentListView(BaseEquipmentListView):
    model = OtherEquipment
    template_name = 'equipments/otherequipment_list.html'
    table_class = OtherEquipmentTable
    filterset_class = ComputerFilter

class OtherEquipmentDetailView(BaseEquipmentDetailView): 
    model = OtherEquipment

class OtherEquipmentCreateView(BaseEquipmentCreateView):
    model = OtherEquipment
    form_class = OtherEquipmentForm

class OtherEquipmentUpdateView(BaseEquipmentUpdateView):
    model = OtherEquipment
    form_class = OtherEquipmentForm

class OtherEquipmentDeleteView(BaseEquipmentDeleteView):
    model = OtherEquipment
    success_url = reverse_lazy('equipments:otherequipment_list')
#Мониторы
class MonitorListView(BaseEquipmentListView):
    model = Monitor
    template_name = 'equipments/monitor_list.html'
    table_class = MonitorTable
    filterset_class = ComputerFilter

class MonitorDetailView(BaseEquipmentDetailView): 
    model = Monitor

class MonitorCreateView(BaseEquipmentCreateView):
    model = Monitor
    form_class = MonitorForm

class MonitorUpdateView(BaseEquipmentUpdateView):
    model = Monitor
    form_class = MonitorForm

class MonitorDeleteView(BaseEquipmentDeleteView):
    model = Monitor
    success_url = reverse_lazy('equipments:monitor_list')