import itertools
import django_tables2 as tables
from .models import Computer, BaseComponent, Equipment, Printer

_TEMPLATE_CMPONENT_LINK = '''<a href="{{ record.get_absolute_url }}">Подробнее</a>'''

class EquipmentTable(tables.Table):
    row_number = tables.Column(empty_values=(), verbose_name='No.')
    view_details = tables.TemplateColumn('''<a href="{{ record.get_absolute_url }}">Подробнее</a>''', verbose_name='Детали')

    def render_row_number(self):
        self.row_counter = getattr(self, 'row_counter', itertools.count())
        return next(self.row_counter)

class ComputerTable(EquipmentTable):

    class Meta:
        model = Computer

class PrinterTable(EquipmentTable):

    class Meta:
        model = Printer


class ComputerComponentsTable(tables.Table):
    row_number = tables.Column(empty_values=(), verbose_name='No.')
    view_details = tables.TemplateColumn(_TEMPLATE_CMPONENT_LINK, verbose_name='Components')

    class Meta: 
        model = BaseComponent
    
    def render_row_number(self):
        self.row_counter = getattr(self, 'row_counter', itertools.count())
        return next(self.row_counter)
