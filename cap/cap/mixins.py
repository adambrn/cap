from django.shortcuts import render
from django.views.generic.base import ContextMixin
from catalogs.models import Motherboard, Processor, RAM, GraphicsCard, Storage, PowerSupply, Cooler, Case, NetworkCard

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
  {'title': 'Главная', 'url': '#'},
  {'title': 'О компании', 'url': '#'},
  {'title': 'Контакты', 'url': '#'},
  {'title': 'Каталог', 'url': '#'}
]
  top_menu = [
  {'title': 'Главная', 'url': 'catalogs:index'},
  {'title': 'Компьютеры', 'url': 'catalogs:computer_list'},
  {'title': 'Принтеры', 'url': 'catalogs:printer_list'},
  {'title': 'Компоненты', 'url': 'catalogs:components'},

  ]


  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['top_menu'] = self.top_menu
    context['menu'] = self.menu
    return context
  