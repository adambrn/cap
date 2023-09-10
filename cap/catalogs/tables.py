import itertools
import django_tables2 as tables
from .models import *

_TEMPLATE_CMPONENT_LINK = '''
        <a href="{{ record.get_absolute_url }}" class="btn btn-link"><i class="fas fa-eye"></i></a>
        <a href="{{ record.get_update_url }}" class="btn btn-link"><i class="fas fa-pencil-alt"></i></a>
        <a href="{{ record.get_delete_url }}" class="btn btn-link"><i class="fas fa-trash-alt"></i></a>
        '''

#Справочники
class CatalogsTable(tables.Table):
    row_number = tables.Column(empty_values=(), verbose_name='No.', orderable=False)
    view_details = tables.TemplateColumn(_TEMPLATE_CMPONENT_LINK, verbose_name='Components')
    class Meta:
        fields = ('row_number',
                    'name', 
                    'view_details',)
    def render_row_number(self):
        self.row_counter = getattr(self, 'row_counter', itertools.count(1))
        return next(self.row_counter)

class ManufacturerTable(CatalogsTable):

    class Meta(CatalogsTable.Meta):
        model = Manufacturer
        verbose_name = "Поизводитель"