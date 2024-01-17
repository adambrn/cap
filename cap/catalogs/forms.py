from django import forms
from .models import *

class BaseCatalogsForm(forms.ModelForm):

    class Meta:
        model = None 
        fields = '__all__'

class ManufacturerForm(BaseCatalogsForm):
    class Meta(BaseCatalogsForm.Meta):
        model = Manufacturer

class EmployeeForm(BaseCatalogsForm):
    class Meta(BaseCatalogsForm.Meta):
        model = Employee

class LocationForm(BaseCatalogsForm):
    class Meta(BaseCatalogsForm.Meta):
        model = Location

# Классы форм для остальных каталогов
class EquipmentCategoryForm(BaseCatalogsForm):
    class Meta(BaseCatalogsForm.Meta):
        model = EquipmentCategory


class EquipmentStatusForm(BaseCatalogsForm):
    class Meta(BaseCatalogsForm.Meta):
        model = EquipmentStatus


class ComponentStatusForm(BaseCatalogsForm):
    class Meta(BaseCatalogsForm.Meta):
        model = ComponentStatus


class MemoryTypeForm(BaseCatalogsForm):
    class Meta(BaseCatalogsForm.Meta):
        model = MemoryType


class StorageTypeForm(BaseCatalogsForm):
    class Meta(BaseCatalogsForm.Meta):
        model = StorageType


class SocketTypeForm(BaseCatalogsForm):
    class Meta(BaseCatalogsForm.Meta):
        model = SocketType
