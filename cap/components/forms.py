from django import forms
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
}