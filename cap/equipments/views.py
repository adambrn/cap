from django.apps import apps
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse_lazy
from django.views import View
from django_filters.views import FilterView
from django.views.generic.edit import FormView

from components.forms import ComponentSelectForm
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
            MonitorTable(Printer.objects.all()),
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
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            
            model_name = (self.model.__name__).lower()  # Имя модели
            context['model_name'] = model_name
            # Получаем текущую дату и время
            current_date = timezone.now()
            # имя атрибута динамически на основе model_name
            equipment_history_attr = model_name + 'history_set'

            # getattr для доступа к связанным записям
            equipment_history = getattr(self.object, equipment_history_attr)

            # словарь аргументов для фильтрации
            filter_args = {
                f"{model_name.lower()}": self.object,
                    'start_date__lte': current_date
            }
            # Получаем последнюю запись истории для данного компьютера на текущую дату
            last_history_entry = equipment_history.filter(**filter_args).aggregate(Max('start_date'))

            if last_history_entry['start_date__max']:
                # словарь аргументов для фильтрации
                filter_args = {
                    f"{model_name.lower()}": self.object,
                    'start_date': last_history_entry['start_date__max']
                }

                # двойная распаковку для передачи аргументов filter
                last_history_entry = equipment_history.filter(**filter_args).last()

            context['current_history'] = last_history_entry
            
            return context

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
    
    def get_tables(self):
        computer_id = self.kwargs.get('pk')
        computer = Computer.objects.get(pk=computer_id)
        tables = [
            ProcessorInComputerTable(Processor.objects.filter(in_computer=computer)),
            RAMInComputerTable(RAM.objects.filter(in_computer=computer)),
            MotherboardInComputerTable(Motherboard.objects.filter(in_computer=computer)),
            GraphicsCardInComputerTable(GraphicsCard.objects.filter(in_computer=computer)),
            StorageInComputerTable(Storage.objects.filter(in_computer=computer)), 
            PowerSupplyInComputerTable(PowerSupply.objects.filter(in_computer=computer)),
            CoolerInComputerTable(Cooler.objects.filter(in_computer=computer)),
            CaseInComputerTable(Case.objects.filter(in_computer=computer)),
            NetworkCardInComputerTable(NetworkCard.objects.filter(in_computer=computer)), 
            OtherComponentInComputerTable(OtherComponent.objects.filter(in_computer=computer)),
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

#Для добавления и удаления компонентов из компьютера
class ComponentRemoveFromComputerView(View):
 def get(self, request, pk, component_pk, component):
        
        # Определяем класс компонента на основе переданного значения
        component_class = COMPONENTS_LIST[component] 
        selected_component = get_object_or_404(component_class, pk=component_pk)
        # Получаем компьютер
        computer = get_object_or_404(Computer, pk=self.kwargs['pk'])


        # Удалить компонент из компьютера 
        selected_component.in_computer = None
        selected_component.save()

        # запись в историю
        selected_component_name = selected_component.__class__.__name__
        model_class = apps.get_model('history', f'{selected_component_name}History')
        fields_to_set = {
            selected_component_name.lower(): selected_component,
            'computer': computer,
            'at_date': timezone.now(),
            'user': self.request.user,
            }

        history_instance = model_class(**fields_to_set)
        history_instance.save()

        return redirect('equipments:computer_detail', pk=pk)

class ComponentAddInComputerView(BaseBreadcrumbMixin, BaseEquipmentMixin, FormView):
    template_name = 'components/add_component.html'
    form_class = ComponentSelectForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        component_class_name = self.kwargs.get('component')

        # Определяем класс компонента на основе переданного значения
        component_class = COMPONENTS_LIST[component_class_name] 
        # Передаем класс компонента в форму через аргумент формы
        kwargs['component_class'] = component_class
        return kwargs
    
    def form_valid(self, form):
        # Получаем компьютер
        computer = get_object_or_404(Computer, pk=self.kwargs['pk'])

        # Выбранный компонент
        selected_component = form.cleaned_data['component']
              
       # Устанавливаем компьютер для выбранного компонента
        selected_component.in_computer = computer
        selected_component.save()

        self.success_url = reverse_lazy('equipments:computer_detail', kwargs={'pk': computer.pk})
        
        # запись в историю
        selected_component_name = selected_component.__class__.__name__
        model_class = apps.get_model('history', f'{selected_component_name}History')
        fields_to_set = {
            selected_component_name.lower(): selected_component,
            'computer': computer,
            'at_date': timezone.now(),
            'user': self.request.user,
            }

        history_instance = model_class(**fields_to_set)
        history_instance.save()

        return super().form_valid(form)
    
    @cached_property
    def crumbs(self):
        computer = get_object_or_404(Computer, pk=self.kwargs['pk'])
        return [("Компьютеры", reverse_lazy('equipments:equipments')),
                (computer.name ,reverse_lazy('equipments:computer_detail', kwargs={'pk': self.kwargs['pk']})),
                (f"Добавить компонент в компьютер" , reverse_lazy('components:component_add_in_computer', kwargs={'pk': self.kwargs['pk'], 'component': self.kwargs['component']})),
                ]
        
