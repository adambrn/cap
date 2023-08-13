import itertools
import django_tables2 as tables
from .models import Computer, BaseComponent

_TEMPLATE_CMPONENT_LINK = '''<a href="{{ record.get_absolute_url }}">Подробнее</a>'''

class ComputerTable(tables.Table):
    row_number = tables.Column(empty_values=(), verbose_name='No.')
    view_components = tables.LinkColumn('catalogs:equipment_components', args=[tables.A('pk')], text='View Components', verbose_name='Components')

    class Meta:
        model = Computer
        template_name = "django_tables2/bootstrap.html"

    def render_row_number(self):
        self.row_counter = getattr(self, 'row_counter', itertools.count())
        return next(self.row_counter)

class ComputerComponentsTable(tables.Table):
    row_number = tables.Column(empty_values=(), verbose_name='No.')
    view_details = tables.TemplateColumn(_TEMPLATE_CMPONENT_LINK, verbose_name='Components')

    class Meta: 
        template_name = "django_tables2/bootstrap.html"
        model = BaseComponent
    def render_row_number(self):
        self.row_counter = getattr(self, 'row_counter', itertools.count())
        return next(self.row_counter)
