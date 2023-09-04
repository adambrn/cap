from django.shortcuts import render
from django.views.generic.base import ContextMixin
from catalogs.models import *
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
  {'title': 'Оборудование', 'url': 'catalogs:equipments'},
  {'title': 'Компоненты', 'url': 'catalogs:components'},

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