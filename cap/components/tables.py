import itertools
import django_tables2 as tables
from .models import *

_TEMPLATE_COMPONENT_LINK = '<a href="{{ record.get_absolute_url }}" class="btn btn-link"><i class="fas fa-eye"></i></a>'

#Компоненты
class ComputerComponentsTable(tables.Table):
    row_number = tables.Column(empty_values=(), verbose_name='No.', orderable=False)
    view_details = tables.TemplateColumn(_TEMPLATE_COMPONENT_LINK, verbose_name='Детали')
    class Meta:
        fields = ('row_number',
                'name',
                'manufacturer',
                'component_status', 
                'view_details',)

    def render_row_number(self):
        self.row_counter = getattr(self, 'row_counter', itertools.count(1))
        return next(self.row_counter)

class MotherboardTable(ComputerComponentsTable):

    class Meta(ComputerComponentsTable.Meta):
        model = Motherboard
        verbose_name = "Материнские платы"

class ProcessorTable(ComputerComponentsTable):
    class Meta(ComputerComponentsTable.Meta):
        model = Processor
        verbose_name = "Процессоры"

class RAMTable(ComputerComponentsTable):
    class Meta(ComputerComponentsTable.Meta):
        model = RAM
        verbose_name = "Оперативная память"

class GraphicsCardTable(ComputerComponentsTable):
    class Meta(ComputerComponentsTable.Meta):
        model = GraphicsCard
        verbose_name = "Видеокарты"
       
class StorageTable(ComputerComponentsTable):
    class Meta(ComputerComponentsTable.Meta):
        model = Storage
        verbose_name = "Накопители"

class PowerSupplyTable(ComputerComponentsTable):
    class Meta(ComputerComponentsTable.Meta):
        model = PowerSupply
        verbose_name = "Блоки питания"
   
class CoolerTable(ComputerComponentsTable):
    class Meta(ComputerComponentsTable.Meta):
        model = Cooler
        verbose_name = "Охлаждение"

class CaseTable(ComputerComponentsTable):
    class Meta(ComputerComponentsTable.Meta):
        model = Case
        verbose_name = "Корпуса"

class NetworkCardTable(ComputerComponentsTable):
    class Meta(ComputerComponentsTable.Meta):
        model = NetworkCard
        verbose_name = "Сетевые карты"

#Таблицы для отображения компонентов в компьютере

_TEMPLATE_COMPONENT_LINKS = '''
<a href="{{ record.get_absolute_url }}" class="btn btn-link"><i class="fas fa-pen"></i></a>
<a href="{{ record.get_absolute_url }}" class="btn btn-link"><i class="fas fa-eye"></i></a>
<a href="{{ record.get_absolute_url }}" class="btn btn-link"><i class="fas fa-trash"></i></a>
'''

#Компоненты
class ComponentsInComputerTable(tables.Table):
    row_number = tables.Column(empty_values=(), verbose_name='No.', orderable=False)
    view_details = tables.TemplateColumn(_TEMPLATE_COMPONENT_LINKS, verbose_name='Детали')
    class Meta:
        model = Computer
        model_name = model.__name__
    
        fields = ('row_number',
                'name',
                'manufacturer',
                'component_status', 
                'view_details',)

    def render_row_number(self):
        self.row_counter = getattr(self, 'row_counter', itertools.count(1))
        return next(self.row_counter)

class MotherboardInComputerTable(ComponentsInComputerTable):

    class Meta(ComponentsInComputerTable.Meta):
        model = Motherboard
        verbose_name = "Материнские платы"

class ProcessorInComputerTable(ComponentsInComputerTable):
    class Meta(ComponentsInComputerTable.Meta):
        model = Processor
        verbose_name = "Процессоры"

class RAMInComputerTable(ComponentsInComputerTable):
    class Meta(ComponentsInComputerTable.Meta):
        model = RAM
        verbose_name = "Оперативная память"
        

class GraphicsCardInComputerTable(ComponentsInComputerTable):
    class Meta(ComponentsInComputerTable.Meta):
        model = GraphicsCard
        verbose_name = "Видеокарты"

class StorageInComputerTable(ComponentsInComputerTable):
    class Meta(ComponentsInComputerTable.Meta):
        model = Storage
        verbose_name = "Накопители"

class PowerSupplyInComputerTable(ComponentsInComputerTable):
    class Meta(ComponentsInComputerTable.Meta):
        model = PowerSupply
        verbose_name = "Блоки питания"

class CoolerInComputerTable(ComponentsInComputerTable):
    class Meta(ComponentsInComputerTable.Meta):
        model = Cooler
        verbose_name = "Охлаждение"

class CaseInComputerTable(ComponentsInComputerTable):
    class Meta(ComponentsInComputerTable.Meta):
        model = Case
        verbose_name = "Корпуса"

class NetworkCardInComputerTable(ComponentsInComputerTable):
    class Meta(ComponentsInComputerTable.Meta):
        model = NetworkCard
        verbose_name = "Сетевые карты"