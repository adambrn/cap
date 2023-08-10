from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView
from django_tables2 import SingleTableView

from .tables import BaseComponentTable
from .models import BaseComponent, Equipment, Motherboard, Processor, RAM, GraphicsCard, Storage, PowerSupply, Cooler, Case, NetworkCard
from django.contrib.auth.mixins import LoginRequiredMixin
components_name = [Motherboard, Processor, RAM, GraphicsCard, Storage, PowerSupply, Cooler, Case, NetworkCard]
class EquipmentCatalogView(LoginRequiredMixin, ListView):
    template_name = 'catalog.html'
    model = Equipment

class EquipmentComponentsView(LoginRequiredMixin, View):
    template_name = 'equipment_components.html'

    def get(self, request, equipment_id, *args, **kwargs):
        try:
            equipment = Equipment.objects.get(id=equipment_id)
            components = components = BaseComponent.objects.filter(in_equipment=equipment)

            context = {
                'equipment': equipment,
                'components': components,
            }
            return render(request, self.template_name, context)
        except Equipment.DoesNotExist:
            # Оборудование не найдено, обработайте эту ситуацию по вашему усмотрению
            pass


class ComponentListView(SingleTableView):
  model = BaseComponent
  table_class = BaseComponentTable
  template_name = 'components.html'

class ComponentDetailView(DetailView):
  model = BaseComponent
  template_name = 'component_detail.html'

class MyLoginView(LoginView):
    template_name = 'accounts/login.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        return context


class MyLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Выход'
        return context