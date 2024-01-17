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
        verbose_name = "Производители"

class EmployeeTable(CatalogsTable):

    class Meta(CatalogsTable.Meta):
        model = Employee
        verbose_name = "Сотрудники"

class LocationTable(CatalogsTable):

    class Meta(CatalogsTable.Meta):
        model = Location
        verbose_name = "Местоположение"

# Классы таблиц для остальных каталогов
class EquipmentCategoryTable(CatalogsTable):

    class Meta(CatalogsTable.Meta):
        model = EquipmentCategory
        verbose_name = "Категория оборудования"


class EquipmentStatusTable(CatalogsTable):

    class Meta(CatalogsTable.Meta):
        model = EquipmentStatus
        verbose_name = "Статус оборудования"


class ComponentStatusTable(CatalogsTable):

    class Meta(CatalogsTable.Meta):
        model = ComponentStatus
        verbose_name = "Статус компонента"


class MemoryTypeTable(CatalogsTable):

    class Meta(CatalogsTable.Meta):
        model = MemoryType
        verbose_name = "Тип памяти"


class StorageTypeTable(CatalogsTable):

    class Meta(CatalogsTable.Meta):
        model = StorageType
        verbose_name = "Тип накопителя"


class SocketTypeTable(CatalogsTable):

    class Meta(CatalogsTable.Meta):
        model = SocketType
        verbose_name = "Тип сокета"
