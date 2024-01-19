import itertools
import django_tables2 as tables
from .models import *

_TEMPLATE_CMPONENT_LINK = '<a href="{{ record.get_absolute_url }}" class="btn btn-link"><i class="fas fa-eye">'
# Оборудование
class EquipmentTable(tables.Table):
    row_number = tables.Column(empty_values=(), verbose_name='No.', orderable=False)
    view_details = tables.TemplateColumn(_TEMPLATE_CMPONENT_LINK, verbose_name='Детали', orderable=False)
    
    class Meta:
        
        fields = ('row_number',
                    'name',
                    'category',
                    'equipment_status', 
                    'view_details',)
    
    def render_row_number(self):
        self.row_counter = getattr(self, 'row_counter', itertools.count(1))
        return next(self.row_counter)

class ComputerTable(EquipmentTable):

    class Meta(EquipmentTable.Meta):
        model = Computer
        verbose_name = "Компьютеры"

class PrinterTable(EquipmentTable):

    class Meta(EquipmentTable.Meta):
        model = Printer
        verbose_name = "Принтеры"

class MonitorTable(EquipmentTable):

    class Meta(EquipmentTable.Meta):
        model = Monitor
        verbose_name = "Мониторы"


class NetworkDeviceTable(EquipmentTable):

    class Meta(EquipmentTable.Meta):
        model = NetworkDevice
        verbose_name = "Сетевое борудование"

class PhoneTable(EquipmentTable):

    class Meta(EquipmentTable.Meta):
        model = Phone
        verbose_name = "Телефоны"

class OtherEquipmentTable(EquipmentTable):

    class Meta(EquipmentTable.Meta):
        model = OtherEquipment
        verbose_name = "Другое оборудование"


class PeripheralsTable(tables.Table):
    row_number = tables.Column(empty_values=(), verbose_name='No.', orderable=False)
    view_details = tables.TemplateColumn(_TEMPLATE_CMPONENT_LINK, verbose_name='Peripherals', orderable=False)

    class Meta:
        model = Peripherals
        fields = ('row_number',
                    'name',
                    'category',
                    'equipment_status', 
                    'view_details',)
        
        verbose_name = "Периферийные устройства"
    def render_row_number(self):
        self.row_counter = getattr(self, 'row_counter', itertools.count())
        return next(self.row_counter)

