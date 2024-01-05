from django.shortcuts import render
from django.views.generic.base import ContextMixin
from catalogs.models import *
from components.models import *
from equipments.models import *
from django.contrib.auth.mixins import LoginRequiredMixin

COMPONENTS_LIST = {
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

class BaseContextMixin(ContextMixin):
  menu = [
  
]
  top_menu = [
    
  {'title': 'Главная', 'url': 'index'},
  {'title': 'Оборудование', 'url': 'equipments:equipments'},
  {'title': 'Компоненты', 'url': 'components:components'},
  {'title': 'Справочники', 'url': 'catalogs:catalogs'},

  ]


  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['top_menu'] = self.top_menu
    context['menu'] = self.menu
    return context
  
class BaseComponentMixin(BaseContextMixin, LoginRequiredMixin):
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
  
class BaseCatalogMixin(BaseContextMixin, LoginRequiredMixin):
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['menu'] =  [
          {'title': 'Производители', 'url': 'catalogs:manufacturer_list'},
          {'title': 'Сотрудники', 'url': 'catalogs:employee_list'},
          {'title': 'Местоположение', 'url': 'catalogs:location_list'},

          ]
    
      return context

class BaseEquipmentMixin(BaseContextMixin, LoginRequiredMixin):
  def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['menu'] =  [
              {'title': 'Компьютеры', 'url': 'equipments:computer_list'},
              {'title': 'Мониторы', 'url': 'equipments:monitor_list'},
              {'title': 'Принтеры', 'url': 'equipments:printer_list'},
              {'title': 'Сетевые устройства', 'url': 'equipments:networkdevice_list'},
              {'title': 'Телефоны', 'url': 'equipments:phone_list'},
              {'title': 'Другие устройства', 'url': 'equipments:otherequipment_list'},
              ]
      
          return context
  

class BaseHistoryMixin(BaseContextMixin, LoginRequiredMixin):
  def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['menu'] =  [
              {'title': 'Компьютеров', 'url': 'history:history'},
              
              ]
      
          return context