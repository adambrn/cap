from django import forms
from .models import *

class BaseEquipmentForm(forms.ModelForm):

    class Meta:
        model = None 
        fields = '__all__'

class ComputerForm(BaseEquipmentForm):
    class Meta(BaseEquipmentForm.Meta):
        model = Computer
