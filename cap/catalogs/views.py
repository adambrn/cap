from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views import View
from .form import BaseComponentForm, COMPONENT_FORMS
from cap.mixins import BaseContextMixin, COMPONENTS_LIST
from .tables import ComputerComponentsTable, ComputerTable
from .models import BaseComponent, Computer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView
from django_tables2 import SingleTableView
from django.views.generic.base import TemplateView

from django.views.generic import DetailView

class EquipmentCatalogView(BaseContextMixin, LoginRequiredMixin, SingleTableView):
    template_name = 'catalog.html'
    table_class = ComputerTable
    model = Computer
    
class ComputerComponentsView(BaseContextMixin, SingleTableView):
    
    model = Computer
    template_name = 'equipment_components.html'
    context_object_name = 'computer'  # Указываем имя переменной в контексте
    table_class = ComputerComponentsTable

    def get_queryset(self):
        computer_id = self.kwargs.get('pk')
        components = []
        computer = Computer.objects.get(pk=computer_id)
        
        for component_name in COMPONENTS_LIST.keys():
            component_set_name = component_name.lower() + "_set"
            if hasattr(computer, component_set_name):
                components.extend(getattr(computer, component_set_name).all())
        
        return components
#Component
class ComponentListView(BaseContextMixin, LoginRequiredMixin, SingleTableView):

  table_class = ComputerComponentsTable
  template_name = 'components.html'
    
  def get_queryset(self):
      components = []     
      for component_name in COMPONENTS_LIST.values():
          components.extend(component_name.objects.all())   
      return components

class ComponentDetailView(BaseContextMixin, LoginRequiredMixin, DetailView):
    
    template_name = 'component_detail.html'
    def get_queryset(self):
        model_name = self.kwargs['model']
        model = COMPONENTS_LIST.get(model_name)
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

    def form_valid(self, form):
        component_type = self.kwargs['component_type']
        model = COMPONENTS_LIST.get(component_type)
        if model:
            component = form.save(commit=False)
            component_instance = model.objects.create(**form.cleaned_data)
            return super().form_valid(form)

        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('component-list')  # Замените на свой URL   

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