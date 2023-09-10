from django import forms
from .models import *

class BaseCatalogsForm(forms.ModelForm):

    class Meta:
        model = None 
        fields = '__all__'

class ManufacturerForm(BaseCatalogsForm):
    class Meta(BaseCatalogsForm.Meta):
        model = Manufacturer
