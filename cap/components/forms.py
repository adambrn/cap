from django import forms

from cap.mixins import COMPONENTS_LIST
from .models import *

class BaseComponentForm(forms.ModelForm):

    class Meta:
        model = None 
        fields = '__all__'

class MotherboardForm(BaseComponentForm):
    class Meta(BaseComponentForm.Meta):
        model = Motherboard

class ProcessorForm(BaseComponentForm):
    class Meta(BaseComponentForm.Meta):
        model = Processor
        
class RAMForm(BaseComponentForm):
    class Meta(BaseComponentForm.Meta):
        model = RAM

class GraphicsCardForm(BaseComponentForm):
    class Meta(BaseComponentForm.Meta):
        model = GraphicsCard

class StorageForm(BaseComponentForm):
    class Meta(BaseComponentForm.Meta):
        model = Storage

class PowerSupplyForm(BaseComponentForm):
    class Meta(BaseComponentForm.Meta):
        model = PowerSupply

class CoolerForm(BaseComponentForm):
    class Meta(BaseComponentForm.Meta):
        model = Cooler

class CaseForm(BaseComponentForm):
    class Meta(BaseComponentForm.Meta):
        model = Case

class NetworkCardForm(BaseComponentForm):
    class Meta(BaseComponentForm.Meta):
        model = NetworkCard

class OtherComponentForm(BaseComponentForm):
    class Meta(BaseComponentForm.Meta):
        model = OtherComponent

COMPONENT_FORMS = {
    'motherboard': MotherboardForm,
    'processor': ProcessorForm,
    'ram': RAMForm,
    'graphicscard': GraphicsCardForm,
    'storage': StorageForm,
    'powersupply': PowerSupplyForm,
    'cooler': CoolerForm,
    'case': CaseForm,
    'networkcard': NetworkCardForm,
    'othercomponent': OtherComponentForm,
}

class ComponentSelectForm(forms.Form):
    component = forms.ModelChoiceField(queryset=None, empty_label=None)

    def __init__(self, *args, **kwargs):
        # Получаем класс компонента из параметра, переданного в конструктор формы
        component_class = kwargs.pop('component_class', None)
        
        super().__init__(*args, **kwargs)
        print(component_class)
        # Проверяем, что класс компонента передан и соответствует ожидаемым классам
        if component_class and component_class in COMPONENTS_LIST.values():
            # Фильтруем queryset на основе класса компонента
            self.fields['component'].queryset = component_class.objects.filter(in_computer__isnull=True)
        else:
            raise ValueError("Invalid component class")