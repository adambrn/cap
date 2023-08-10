import django_tables2 as tables
from .models import Equipment, BaseComponent

class EquipmentTable(tables.Table):
    class Meta:
        model = Equipment
        template_name = "django_tables2/bootstrap.html"
        fields = ('id', 'model', 'manufacturer', 'serial_number')

class BaseComponentTable(tables.Table):
    class Meta:
        model = BaseComponent 
        template_name = "django_tables2/bootstrap.html"
        fields = ('id', 'name', 'manufacturer', 'serial_number')