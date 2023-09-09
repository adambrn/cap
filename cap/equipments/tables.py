import itertools
import django_tables2 as tables
from .models import *

_TEMPLATE_CMPONENT_LINK = '''<a href="{{ record.get_absolute_url }}">Подробнее</a>'''
# Оборудование
class EquipmentTable(tables.Table):
    row_number = tables.Column(empty_values=(), verbose_name='No.')
    view_details = tables.TemplateColumn('''<a href="{{ record.get_absolute_url }}">Подробнее</a>''', verbose_name='Детали')
    
    
    
    def render_row_number(self):
        self.row_counter = getattr(self, 'row_counter', itertools.count())
        return next(self.row_counter)

class ComputerTable(EquipmentTable):

    class Meta:
        model = Computer
        verbose_name = "Компьютеры"
      
class PrinterTable(EquipmentTable):

    class Meta:
        model = Printer
        verbose_name = "Принтеры"

class NetworkDeviceTable(EquipmentTable):

    class Meta:
        model = NetworkDevice
        verbose_name = "Сетевое борудование"

class PhoneTable(EquipmentTable):

    class Meta:
        model = Phone
        verbose_name = "Телефоны"

class OtherEquipmentTable(EquipmentTable):

    class Meta:
        model = OtherEquipment
        verbose_name = "Другое оборудование"


class PeripheralsTable(tables.Table):
    row_number = tables.Column(empty_values=(), verbose_name='No.', orderable=False)
    view_details = tables.TemplateColumn(_TEMPLATE_CMPONENT_LINK, verbose_name='Peripherals')

    class Meta:
        model = Peripherals
        verbose_name = "Периферийные устройства"
        def render_row_number(self):
            self.row_counter = getattr(self, 'row_counter', itertools.count())
            return next(self.row_counter)

