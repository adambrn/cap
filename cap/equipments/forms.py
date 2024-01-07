from django import forms

from components.models import get_datetime_now
from .models import *




class BaseEquipmentForm(forms.ModelForm):
    purchase_date = forms.DateTimeField(required=False, label='Дата начала использования', initial=get_datetime_now, widget=forms.DateTimeInput(attrs={'type': 'datetime'}))
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