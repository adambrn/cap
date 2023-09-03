from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django_filters.views import FilterView

from .filters import *
from .form import BaseComponentForm, COMPONENT_FORMS
from cap.mixins import BaseContextMixin, COMPONENTS_LIST
from .tables import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, ListView
from django_tables2 import MultiTableMixin, SingleTableMixin, SingleTableView
from django.views.generic.base import TemplateView
from view_breadcrumbs import DetailBreadcrumbMixin, BaseBreadcrumbMixin
from view_breadcrumbs.generic.base import BaseModelBreadcrumbMixin
from django.utils.functional import cached_property

from django.views.generic import DetailView

class Index(BaseContextMixin, LoginView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context

class EquipmentCatalogView(BaseBreadcrumbMixin, BaseContextMixin, LoginRequiredMixin, MultiTableMixin, TemplateView):
    
    template_name = 'equipments.html'
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
            {'title': 'Компьютеры', 'url': 'catalogs:computer_list'},
            {'title': 'Принтеры', 'url': 'catalogs:printer_list'},
            {'title': 'Сетевые устройства', 'url': 'catalogs:network_device_list'},
            {'title': 'Телефоны', 'url': 'catalogs:phone_list'},
            {'title': 'Другие устройства', 'url': 'catalogs:other_equipment_list'},
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
            {'title': 'Компьютеры', 'url': 'catalogs:computer_list'},
            {'title': 'Принтеры', 'url': 'catalogs:printer_list'},
            {'title': 'Сетевые устройства', 'url': 'catalogs:network_device_list'},
            {'title': 'Телефоны', 'url': 'catalogs:phone_list'},
            {'title': 'Другие устройства', 'url': 'catalogs:other_equipment_list'},
            ]
     
        return context
    
    @cached_property
    def crumbs(self):
        return [("Обрудование", "/catalogs/"), (self.model_name_title_plural, "/")]

class EquipmentDetailView(DetailBreadcrumbMixin, BaseContextMixin, LoginRequiredMixin, DetailView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] =  [
            {'title': 'Компьютеры', 'url': 'catalogs:computer_list'},
            {'title': 'Принтеры', 'url': 'catalogs:printer_list'},
            {'title': 'Сетевые устройства', 'url': 'catalogs:network_device_list'},
            {'title': 'Телефоны', 'url': 'catalogs:phone_list'},
            {'title': 'Другие устройства', 'url': 'catalogs:other_equipment_list'},
            ]
     
        return context

#Компьютеры
class ComputersView(EquipmentView):
    model = Computer
    template_name = 'computers.html'
    table_class = ComputerTable
    filterset_class = ComputerFilter

class ComputerDetailView(MultiTableMixin,EquipmentDetailView):
    
    model = Computer
    template_name = 'computer_detail.html'

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
    template_name = 'computers.html'
    table_class = PrinterTable
    filterset_class = ComputerFilter  

class PrinterDetailView(EquipmentDetailView):
    
    model = Printer
    template_name = 'printer_detail.html'

#Сетевое оборудование
class NetworkDeviceView(EquipmentView):
    model = NetworkDevice
    template_name = 'network_device.html'
    table_class = NetworkDeviceTable
    filterset_class = ComputerFilter

class NetworkDeviceDetailView(EquipmentDetailView): 
    model = NetworkDevice
    template_name = 'network_device_detail.html'

#Телефоны
class PhoneView(EquipmentView):
    model = Phone
    template_name = 'phone.html'
    table_class = PhoneTable
    filterset_class = ComputerFilter

class PhoneDetailView(EquipmentDetailView): 
    model = Phone
    template_name = 'phone_detail.html'

#Другое оборудование
class OtherEquipmentView(EquipmentView):
    model = OtherEquipment
    template_name = 'other_equipment.html'
    table_class = OtherEquipmentTable
    filterset_class = ComputerFilter

class OtherEquipmentDetailView(EquipmentDetailView): 
    model = OtherEquipment
    template_name = 'other_equipment_detail.html'


#Базовые классы компонентов
class BaseComponentView(BaseModelBreadcrumbMixin, BaseContextMixin, LoginRequiredMixin, SingleTableMixin, FilterView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] =  [
            {'title': 'Процессоры', 'url': 'catalogs:processor_list'},
            {'title': 'Оперативная память', 'url': 'catalogs:ram_list'},
            {'title': 'Материнские платы', 'url': 'catalogs:motherboard_list'},
            {'title': 'Видеокарты', 'url': 'catalogs:graphicscard_list'},
            {'title': 'Накопители', 'url': 'catalogs:storage_list'},
            {'title': 'Блоки питания', 'url': 'catalogs:powersupply_list'},
            {'title': 'Охлаждение', 'url': 'catalogs:cooler_list'}, 
            {'title': 'Корпуса', 'url': 'catalogs:case_list'},
            {'title': 'Сетевые карты', 'url': 'catalogs:networkcard_list'},
            ]
     
        return context
    
    @cached_property
    def crumbs(self):
        return [("Компоненты", reverse_lazy("catalogs:components")), (self.model_name_title_plural, "/")]

class BaseComponentDetailView(DetailBreadcrumbMixin, BaseContextMixin, LoginRequiredMixin, DetailView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] =  [
            {'title': 'Процессоры', 'url': 'catalogs:processor_list'},
            {'title': 'Оперативная память', 'url': 'catalogs:ram_list'},
            {'title': 'Материнские платы', 'url': 'catalogs:motherboard_list'},
            {'title': 'Видеокарты', 'url': 'catalogs:graphicscard_list'},
            {'title': 'Накопители', 'url': 'catalogs:storage_list'},
            {'title': 'Блоки питания', 'url': 'catalogs:powersupply_list'},
            {'title': 'Охлаждение', 'url': 'catalogs:cooler_list'}, 
            {'title': 'Корпуса', 'url': 'catalogs:case_list'},
            {'title': 'Сетевые карты', 'url': 'catalogs:networkcard_list'},
            ]
     
        return context

#Component
class ProcessorListView(BaseComponentView):
    model = Processor
    template_name = 'components/processor_list.html'
    table_class = ProcessorTable
    filterset_class = ComponentFilter

class ProcessorDetailView(BaseComponentDetailView):
    model = Processor
    template_name = 'components/processor_detail.html'

class MotherboardListView(BaseComponentView):
    model = Motherboard  
    template_name = 'components/motherboard_list.html'
    table_class = MotherboardTable
    filterset_class = ComponentFilter

class MotherboardDetailView(BaseComponentDetailView):
    model = Motherboard
    template_name = 'components/motherboard_detail.html'

class RAMListView(BaseComponentView):
    model = RAM
    template_name = 'components/ram_list.html'
    table_class = RAMTable
    filterset_class = ComponentFilter

class RAMDetailView(BaseComponentDetailView):
    model = RAM
    template_name = 'components/ram_detail.html'

class GraphicsCardListView(BaseComponentView):
    model = GraphicsCard
    template_name = 'components/graphicscard_list.html'
    table_class = GraphicsCardTable
    filterset_class = ComponentFilter

class GraphicsCardDetailView(BaseComponentDetailView):
    model = GraphicsCard 
    template_name = 'components/graphicscard_detail.html'

class StorageListView(BaseComponentView):
    model = Storage
    template_name = 'components/storage_list.html' 
    table_class = StorageTable
    filterset_class = ComponentFilter

class StorageDetailView(BaseComponentDetailView):
    model = Storage 
    template_name = 'components/storage_detail.html'

class PowerSupplyListView(BaseComponentView):
    model = PowerSupply
    template_name = 'components/powersupply_list.html'
    table_class = PowerSupplyTable
    filterset_class = ComponentFilter

class PowerSupplyDetailView(BaseComponentDetailView):
    model = PowerSupply
    template_name = 'components/powersupply_detail.html'

class CoolerListView(BaseComponentView):
    model = Cooler
    template_name = 'components/cooler_list.html'
    table_class = CoolerTable
    filterset_class = ComponentFilter

class CoolerDetailView(BaseComponentDetailView):
    model = Cooler
    template_name = 'components/cooler_detail.html'

class CaseListView(BaseComponentView):
    model = Case  
    template_name = 'components/case_list.html'
    table_class = CaseTable
    filterset_class = ComponentFilter

class CaseDetailView(BaseComponentDetailView):
    model = Case
    template_name = 'components/case_detail.html'

class NetworkCardListView(BaseComponentView):
    model = NetworkCard
    template_name = 'components/networkcard_list.html'
    table_class = NetworkCardTable 
    filterset_class = ComponentFilter

class NetworkCardDetailView(BaseComponentDetailView):
    model = NetworkCard
    template_name = 'components/networkcard_detail.html'


class ComponentListView(BaseBreadcrumbMixin, BaseContextMixin, LoginRequiredMixin, MultiTableMixin, TemplateView):
    template_name = 'components.html'
    
    def get_tables(self):
        tables = [
            ProcessorTable(Processor.objects.all()),
            RAMTable(RAM.objects.all()),
            MotherboardTable(Motherboard.objects.all()),
            GraphicsCardTable(GraphicsCard.objects.all()),
            StorageTable(Storage.objects.all()), 
            PowerSupplyTable(PowerSupply.objects.all()),
            CoolerTable(Cooler.objects.all()),
            CaseTable(Case.objects.all()),
            NetworkCardTable(NetworkCard.objects.all()), 
        ]
        return tables
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] =  [
            {'title': 'Процессоры', 'url': 'catalogs:processor_list'},
            {'title': 'Оперативная память', 'url': 'catalogs:ram_list'},
            {'title': 'Материнские платы', 'url': 'catalogs:motherboard_list'},
            {'title': 'Видеокарты', 'url': 'catalogs:graphicscard_list'},
            {'title': 'Накопители', 'url': 'catalogs:storage_list'},
            {'title': 'Блоки питания', 'url': 'catalogs:powersupply_list'},
            {'title': 'Охлаждение', 'url': 'catalogs:cooler_list'}, 
            {'title': 'Корпуса', 'url': 'catalogs:case_list'},
            {'title': 'Сетевые карты', 'url': 'catalogs:networkcard_list'},
            ]
     
        return context
    
    @cached_property
    def crumbs(self):
        return [("Компоненты", "components/")]
    
class ComponentDetailView(BaseContextMixin, LoginRequiredMixin, DetailBreadcrumbMixin, DetailView):

    template_name = 'component_detail.html'
    #crumbs = [("My Test Breadcrumb", reverse_lazy("/"))]
   
    def get_queryset(self):
        model_name = self.kwargs['model']
        model = COMPONENTS_LIST.get(model_name)
        self.model = model
        if model:
            return model.objects.filter(pk=self.kwargs['pk'])
        return super().get_queryset()
      
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs['model']
        model = COMPONENTS_LIST.get(model_name)
        if model:
            instance = get_object_or_404(model, pk=self.kwargs['pk'])
            context['instance'] = instance
        
        fields_data = []
        m2m_fields = ['supported_memory_types']
        for field in instance._meta.get_fields():
            field_name = field.verbose_name
            field_value = getattr(instance, field.name)
            if field.name in m2m_fields:
                field_value = ", ".join(str(item) for item in field_value.all())
            fields_data.append((field_name, field_value))

        context['fields_data'] = fields_data
        
        return context

class SelectComponentView(BaseContextMixin, LoginRequiredMixin, TemplateView):
    template_name = 'select_component.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        component_list = [(component_type, model._meta.verbose_name) for component_type, model in COMPONENTS_LIST.items()]
        context['component_list'] = component_list
        return context

class CreateComponentView(BaseContextMixin, LoginRequiredMixin, CreateView):
    template_name = 'create_component.html'

    def get_form_class(self):
        component_type = self.kwargs['component_type']
        return COMPONENT_FORMS.get(component_type, BaseComponentForm)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['component_type'] = self.kwargs['component_type']
        return context

    def get_success_url(self):
        return reverse('catalogs:components')

#LOGIN
class BaseLoginView(BaseContextMixin, LoginView):
    template_name = 'accounts/login.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        return context

class BaseLogoutView(BaseContextMixin, LogoutView):
    template_name = 'accounts/logout.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Выход'
        return context