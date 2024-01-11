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
        fields = ('row_number',
                    'computer',
                    'employee',
                    'location', 
                    'start_date',
                    'end_date',
                )

class MonitorHistoryTable(EquipmentHistoryTable):
    class Meta(EquipmentHistoryTable.Meta):
        model = MonitorHistory
        verbose_name = "История Мониторов"
        fields = ('row_number',
                    'monitor',
                    'employee',
                    'location', 
                    'start_date',
                    'end_date',
                )

class PrinterHistoryTable(EquipmentHistoryTable):
    class Meta(EquipmentHistoryTable.Meta):
        model = PrinterHistory
        verbose_name = "История принтеров"
        fields = ('row_number',
                    'printer',
                    'employee',
                    'location', 
                    'start_date',
                    'end_date',
                )

class PhoneHistoryTable(EquipmentHistoryTable):
    class Meta(EquipmentHistoryTable.Meta):
        model = PhoneHistory
        verbose_name = "История телефонов"
        fields = ('row_number',
                    'phone',
                    'employee',
                    'location', 
                    'start_date',
                    'end_date',
                )

class NetworkDeviceHistoryTable(EquipmentHistoryTable):
    class Meta(EquipmentHistoryTable.Meta):
        model = NetworkDeviceHistory
        verbose_name = "История сетевого борудования"
        fields = ('row_number',
                    'networkdevice',
                    'employee',
                    'location', 
                    'start_date',
                    'end_date',
                )

class OtherEquipmentHistoryTable(EquipmentHistoryTable):
    class Meta(EquipmentHistoryTable.Meta):
        model = OtherEquipmentHistory
        verbose_name = "История сетевого борудования"
        fields = ('row_number',
                    'otherequipment',
                    'employee',
                    'location', 
                    'start_date',
                    'end_date',
                )
        
# Таблицы истории компонентов   
class ComponentHistoryTable(tables.Table):
    row_number = tables.Column(empty_values=(), verbose_name='No.')
    #view_details = tables.TemplateColumn(_TEMPLATE_CMPONENT_LINK, verbose_name='Детали')
    
    class Meta:
         fields = ('row_number',
                    'computer',
                    'start_date',
                    'end_date',
                )
    
    def render_row_number(self):
        self.row_counter = getattr(self, 'row_counter', itertools.count(1))
        return next(self.row_counter)

class ProcessorHistoryTable(ComponentHistoryTable):
    class Meta(ComponentHistoryTable.Meta):
        model = ProcessorHistory
        verbose_name = "История процессоров"
        fields = ('row_number',
                    'processor',
                    'computer',
                    
                   'start_date',
                    'end_date',
                )
class MotherboardHistoryTable(ComponentHistoryTable):
    class Meta(ComponentHistoryTable.Meta):
        model = MotherBoardHistory
        verbose_name = "История материнских плат"
        fields = ('row_number', 'motherboard', 'computer',  'start_date', 'end_date',)

class RAMHistoryTable(ComponentHistoryTable):
    class Meta(ComponentHistoryTable.Meta):
        model = RAMHistory
        verbose_name = "История оперативной памяти"
        fields = ('row_number', 'ram', 'computer',  'start_date', 'end_date',)

class StorageHistoryTable(ComponentHistoryTable):
    class Meta(ComponentHistoryTable.Meta):
        model = StorageHistory
        verbose_name = "История жестких дисков"
        fields = ('row_number', 'storage', 'computer',  'start_date', 'end_date',)

class GraphicsCardHistoryTable(ComponentHistoryTable):
    class Meta(ComponentHistoryTable.Meta):
        model = GraphicsCardHistory
        verbose_name = "История видеокарт"
        fields = ('row_number', 'graphicscard', 'computer',  'start_date', 'end_date',)

class CaseHistoryTable(ComponentHistoryTable):
    class Meta(ComponentHistoryTable.Meta):
        model = CaseHistory
        verbose_name = "История корпусов"
        fields = ('row_number', 'case', 'computer',  'start_date', 'end_date',)

class NetworkCardHistoryTable(ComponentHistoryTable):
    class Meta(ComponentHistoryTable.Meta):
        model = NetworkCardHistory
        verbose_name = "История сетевых карт"
        fields = ('row_number', 'networkcard', 'computer',  'start_date', 'end_date',)

class CoolerHistoryTable(ComponentHistoryTable):
    class Meta(ComponentHistoryTable.Meta):
        model = CoolerHistory
        verbose_name = "История кулеров"
        fields = ('row_number', 'cooler', 'computer',  'start_date', 'end_date',)

class OtherComponentHistoryTable(ComponentHistoryTable):
    class Meta(ComponentHistoryTable.Meta):
        model = OtherComponentHistory
        verbose_name = "История других компонентов"
        fields = ('row_number', 'othercomponent', 'computer',  'start_date', 'end_date',)

class PowerSupplyHistoryTable(ComponentHistoryTable):
    class Meta(ComponentHistoryTable.Meta):
        model = PowerSupplyHistory
        verbose_name = "История блоков питания"
        fields = ('row_number', 'powersupply', 'computer','start_date', 'end_date',)