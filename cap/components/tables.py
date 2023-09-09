import itertools
import django_tables2 as tables
from .models import *

_TEMPLATE_CMPONENT_LINK = '''<a href="{{ record.get_absolute_url }}">Подробнее</a>'''

#Компоненты
class ComputerComponentsTable(tables.Table):
    row_number = tables.Column(empty_values=(), verbose_name='No.', orderable=False)
    view_details = tables.TemplateColumn(_TEMPLATE_CMPONENT_LINK, verbose_name='Components')
    
    def render_row_number(self):
        self.row_counter = getattr(self, 'row_counter', itertools.count())
        return next(self.row_counter)

class MotherboardTable(ComputerComponentsTable):

    class Meta:
        model = Motherboard
        verbose_name = "Материнские платы"

class ProcessorTable(ComputerComponentsTable):
    class Meta:
        model = Processor
        verbose_name = "Процессоры"

class RAMTable(ComputerComponentsTable):
    class Meta:
        model = RAM
        verbose_name = "Оперативная память"

class GraphicsCardTable(ComputerComponentsTable):
    class Meta:
        model = GraphicsCard
        verbose_name = "Видеокарты"

class StorageTable(ComputerComponentsTable):
    class Meta:
        model = Storage
        verbose_name = "Накопители"

class PowerSupplyTable(ComputerComponentsTable):
    class Meta:
        model = PowerSupply
        verbose_name = "Блоки питания"

class CoolerTable(ComputerComponentsTable):
    class Meta:
        model = Cooler
        verbose_name = "Охлаждение"

class CaseTable(ComputerComponentsTable):
    class Meta:
        model = Case
        verbose_name = "Корпуса"

class NetworkCardTable(ComputerComponentsTable):
    class Meta:
        model = NetworkCard
        verbose_name = "Сетевые карты"



