import itertools
import django_tables2 as tables
from .models import *

_TEMPLATE_CMPONENT_LINK = '''<a href="{{ record.get_absolute_url }}">Подробнее</a>'''

#Справочники
class CatalogsTable(tables.Table):
    row_number = tables.Column(empty_values=(), verbose_name='No.', orderable=False)
    view_details = tables.TemplateColumn(_TEMPLATE_CMPONENT_LINK, verbose_name='Components')
    
    def render_row_number(self):
        self.row_counter = getattr(self, 'row_counter', itertools.count())
        return next(self.row_counter)

class ManufacturerTable(CatalogsTable):

    class Meta:
        model = Manufacturer
        verbose_name = "Поизводитель"