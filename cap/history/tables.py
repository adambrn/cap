import itertools
import django_tables2 as tables
from .models import *

#_TEMPLATE_CMPONENT_LINK = '<a href="{{ record.get_absolute_url }}" class="btn btn-link"><i class="fas fa-eye">'
# Оборудование
class EquipmentHistoryTable(tables.Table):
    row_number = tables.Column(empty_values=(), verbose_name='No.')
    #view_details = tables.TemplateColumn(_TEMPLATE_CMPONENT_LINK, verbose_name='Детали')
    
    class Meta:
        fields = ('row_number',
                    'computer',
                    'employee',
                    'location', 
                    'start_date',
                    'end_date',
                )
    
    def render_row_number(self):
        self.row_counter = getattr(self, 'row_counter', itertools.count(1))
        return next(self.row_counter)

class ComputerHistoryTable(EquipmentHistoryTable):

    class Meta(EquipmentHistoryTable.Meta):
        model = ComputerHistory
        verbose_name = "История компьютеры"


