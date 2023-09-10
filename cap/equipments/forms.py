from django import forms
from .models import *

class BaseEquipmentForm(forms.ModelForm):

    class Meta:
        model = None 
        fields = '__all__'

class ComputerForm(BaseEquipmentForm):
    class Meta(BaseEquipmentForm.Meta):
        model = Computer

class PrinterForm(BaseEquipmentForm):
    class Meta(BaseEquipmentForm.Meta):
        model = Printer

class NetworkDeviceForm(BaseEquipmentForm):
    class Meta(BaseEquipmentForm.Meta):
        model = NetworkDevice

class MonitorForm(BaseEquipmentForm):
    class Meta(BaseEquipmentForm.Meta):
        model = Monitor

class PhoneForm(BaseEquipmentForm):
    class Meta(BaseEquipmentForm.Meta):
        model = Phone

class OtherEquipmentForm(BaseEquipmentForm):
    class Meta(BaseEquipmentForm.Meta):
        model = OtherEquipment