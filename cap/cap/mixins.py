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
    'othercomponent': OtherComponent
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
          {'title': 'Прочие', 'url': 'components:othercomponent_list'},
          ]
    
      return context
  
class BaseCatalogMixin(BaseContextMixin, LoginRequiredMixin):
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['menu'] = [
          
          {'title': 'Сотрудники', 'url': 'catalogs:employee_list'},
          {'title': 'Местоположение', 'url': 'catalogs:location_list'},
          {'title': 'Производители', 'url': 'catalogs:manufacturer_list'},
          {'title': 'Категории оборудования', 'url': 'catalogs:equipmentcategory_list'},
          {'title': 'Статусы оборудования', 'url': 'catalogs:equipmentstatus_list'},
          {'title': 'Статусы компонентов', 'url': 'catalogs:componentstatus_list'},
          {'title': 'Типы памяти', 'url': 'catalogs:memorytype_list'},
          {'title': 'Типы хранилищ', 'url': 'catalogs:storagetype_list'},
          {'title': 'Типы сокетов', 'url': 'catalogs:sockettype_list'},
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
              {'title': 'Компьютеры', 'url': 'history:all_computer_history_list'},
              {'title': 'Принтеры', 'url': 'history:all_printer_history_list'},
              {'title': 'Мониторы', 'url': 'history:all_monitor_history_list'},
              {'title': 'Телефоны', 'url': 'history:all_phone_history_list'},
              {'title': 'Сетевые устройства', 'url': 'history:all_networkdevice_history_list'},
              {'title': 'Другие устройства', 'url': 'history:all_otherequipment_history_list'},
              ]
      
          return context