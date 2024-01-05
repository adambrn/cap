from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django_filters.views import FilterView
from components.filters import *
from cap.mixins import *
from components.tables import *
from components.models import *
from components.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, ListView, DeleteView, UpdateView
from django_tables2 import MultiTableMixin, SingleTableMixin, SingleTableView
from django.views.generic.base import TemplateView
from view_breadcrumbs import DetailBreadcrumbMixin, BaseBreadcrumbMixin, CreateBreadcrumbMixin, DeleteBreadcrumbMixin, UpdateBreadcrumbMixin
from view_breadcrumbs.generic.base import BaseModelBreadcrumbMixin
from django.utils.functional import cached_property
# Create your views here.
#Базовые классы компонентов
class BaseComponentView(BaseModelBreadcrumbMixin, BaseComponentMixin, SingleTableMixin, FilterView):
 
    @cached_property
    def crumbs(self):
        return [("Компоненты", reverse_lazy("components:components")), (self.model_name_title_plural, "/")]

class BaseComponentDetailView(DetailBreadcrumbMixin, BaseComponentMixin, DetailView):
    pass

class BaseComponentDeleteView(DeleteBreadcrumbMixin, BaseComponentMixin, DeleteView):
    pass

class BaseComponentUpdateView(UpdateBreadcrumbMixin, BaseComponentMixin, UpdateView):
    def get_context_data(self, **kwargs):
        """Add the models verbose name to the context dictionary."""

        kwargs.update({
            "model_verbose_name": self.form_class._meta.model._meta.verbose_name,})
        return super().get_context_data(**kwargs)

class BaseComponentCreateView(CreateBreadcrumbMixin, BaseComponentMixin, CreateView):
    def get_context_data(self, **kwargs):
        """Add the models verbose name to the context dictionary."""

        kwargs.update({
            "model_verbose_name": self.form_class._meta.model._meta.verbose_name,})
        return super().get_context_data(**kwargs)

#Component
#Поцессоры
class ProcessorListView(BaseComponentView):
    model = Processor
    template_name = 'components/processor_list.html'
    table_class = ProcessorTable
    filterset_class = ComponentFilter

class ProcessorDetailView(BaseComponentDetailView):
    model = Processor
    template_name = 'components/processor_detail.html'

class ProcessorCreateView(BaseComponentCreateView):
    model = Processor
    form_class = ProcessorForm
    template_name = 'components/create_component.html'

class ProcessorUpdateView(BaseComponentUpdateView):
    model = Processor
    form_class = ProcessorForm
    template_name = 'components/create_component.html'

class ProcessorDeleteView(BaseComponentDeleteView):
    model = Processor
    success_url = reverse_lazy("components:processor_list")
    template_name = 'components/processor_delete.html'

#Материнские платы
class MotherboardListView(BaseComponentView):
    model = Motherboard  
    template_name = 'components/motherboard_list.html'
    table_class = MotherboardTable
    filterset_class = ComponentFilter

class MotherboardDetailView(BaseComponentDetailView):
    model = Motherboard
    template_name = 'components/motherboard_detail.html'

class MotherboardCreateView(BaseComponentCreateView):
    model = Motherboard
    form_class = MotherboardForm
    template_name = 'components/create_component.html'

class MotherboardUpdateView(BaseComponentUpdateView):
    model = Motherboard
    form_class = MotherboardForm
    template_name = 'components/create_component.html'

class MotherboardDeleteView(BaseComponentDeleteView):
    model = Motherboard
    success_url = reverse_lazy("components:motherboard_list")
    template_name = 'components/motherboard_delete.html'

#Память
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
    template_name = 'components/components.html'
    
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
            {'title': 'Процессоры', 'url': 'components:processor_list'},
            {'title': 'Оперативная память', 'url': 'components:ram_list'},
            {'title': 'Материнские платы', 'url': 'components:motherboard_list'},
            {'title': 'Видеокарты', 'url': 'components:graphicscard_list'},
            {'title': 'Накопители', 'url': 'components:storage_list'},
            {'title': 'Блоки питания', 'url': 'components:powersupply_list'},
            {'title': 'Охлаждение', 'url': 'components:cooler_list'}, 
            {'title': 'Корпуса', 'url': 'components:case_list'},
            {'title': 'Сетевые карты', 'url': 'components:networkcard_list'},
            ]
     
        return context
    
    @cached_property
    def crumbs(self):
        return [("Компоненты", "components/")]
    
class ComponentDetailView(BaseContextMixin, LoginRequiredMixin, DetailBreadcrumbMixin, DetailView):

    template_name = 'components/component_detail.html'
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

class SelectComponentView(BaseBreadcrumbMixin, BaseContextMixin, LoginRequiredMixin, TemplateView):
    template_name = 'components/select_component.html'
    crumbs = [("Компоненты", reverse_lazy("components:components"))]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        component_list = [(component_type, model._meta.verbose_name) for component_type, model in COMPONENTS_LIST.items()]
        context['component_list'] = component_list
        context['menu'] =  [
            {'title': 'Процессоры', 'url': 'components:processor_list'},
            {'title': 'Оперативная память', 'url': 'components:ram_list'},
            {'title': 'Материнские платы', 'url': 'components:motherboard_list'},
            {'title': 'Видеокарты', 'url': 'components:graphicscard_list'},
            {'title': 'Накопители', 'url': 'components:storage_list'},
            {'title': 'Блоки питания', 'url': 'components:powersupply_list'},
            {'title': 'Охлаждение', 'url': 'components:cooler_list'}, 
            {'title': 'Корпуса', 'url': 'components:case_list'},
            {'title': 'Сетевые карты', 'url': 'components:networkcard_list'},
            ]
        return context

class CreateComponentView(CreateBreadcrumbMixin, BaseContextMixin, LoginRequiredMixin, CreateView):
    template_name = 'components/create_component.html'

    def get_form_class(self):
        component_type = self.kwargs['component_type']
        return COMPONENT_FORMS.get(component_type, BaseComponentForm)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['component_type'] = self.kwargs['component_type']
        context['menu'] =  [
            {'title': 'Процессоры', 'url': 'components:processor_list'},
            {'title': 'Оперативная память', 'url': 'components:ram_list'},
            {'title': 'Материнские платы', 'url': 'components:motherboard_list'},
            {'title': 'Видеокарты', 'url': 'components:graphicscard_list'},
            {'title': 'Накопители', 'url': 'components:storage_list'},
            {'title': 'Блоки питания', 'url': 'components:powersupply_list'},
            {'title': 'Охлаждение', 'url': 'components:cooler_list'}, 
            {'title': 'Корпуса', 'url': 'components:case_list'},
            {'title': 'Сетевые карты', 'url': 'components:networkcard_list'},
            ]
        return context

    def get_success_url(self):
        return reverse('components:components')


