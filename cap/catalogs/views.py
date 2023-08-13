from django.shortcuts import get_object_or_404, render
from django.contrib.auth.views import LoginView, LogoutView
from cap.mixins import BaseContextMixin
from django_tables2 import SingleTableView
from .tables import ComputerComponentsTable, ComputerTable
from .models import BaseComponent, Computer, Motherboard, Processor, RAM, GraphicsCard, Storage, PowerSupply, Cooler, Case, NetworkCard
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django_tables2 import SingleTableView


COMPONENTS_NAME = ['Motherboard', 'Processor', 'RAM', 'GraphicsCard', 'Storage', 'PowerSupply', 'Cooler', 'Case', 'NetworkCard']

class EquipmentCatalogView(BaseContextMixin, LoginRequiredMixin, SingleTableView):
    template_name = 'catalog.html'
    table_class = ComputerTable
    model = Computer

from django.views.generic import DetailView
from django_tables2 import SingleTableView
from .models import Computer
from .tables import ComputerComponentsTable

COMPONENTS_NAME = {
    'motherboard': Motherboard,
    'processor': Processor,
    'ram': RAM,
    'graphicscard': GraphicsCard,
    'storage': Storage,
    'powersupply': PowerSupply,
    'cooler': Cooler,
    'case': Case,
    'networkcard': NetworkCard,
}

class ComputerComponentsView(BaseContextMixin, SingleTableView):
    
    model = Computer
    template_name = 'equipment_components.html'
    context_object_name = 'computer'  # Указываем имя переменной в контексте
    table_class = ComputerComponentsTable

    def get_queryset(self):
        computer_id = self.kwargs.get('pk')
        components = []
        computer = Computer.objects.get(pk=computer_id)
        
        for component_name in COMPONENTS_NAME.keys():
            component_set_name = component_name.lower() + "_set"
            if hasattr(computer, component_set_name):
                components.extend(getattr(computer, component_set_name).all())
        
        return components

class ComponentListView(BaseContextMixin, LoginRequiredMixin, SingleTableView):

  table_class = ComputerComponentsTable
  template_name = 'components.html'
    
  def get_queryset(self):
      components = []
      
      for component_name in COMPONENTS_NAME.values():
   
          components.extend(component_name.objects.all())
      
      return components

class ComponentDetailView(BaseContextMixin, LoginRequiredMixin, DetailView):
    
    template_name = 'component_detail.html'
    def get_queryset(self):
        model_name = self.kwargs['model']
        model = COMPONENTS_NAME.get(model_name)
        if model:
            return model.objects.filter(pk=self.kwargs['pk'])
        return super().get_queryset()
      
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs['model']
        model = COMPONENTS_NAME.get(model_name)
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