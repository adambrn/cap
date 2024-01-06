from django import forms
from .models import *

class EmployeeHistoryForm(forms.ModelForm):
    pass

class EmployeeComputerHistoryForm(EmployeeHistoryForm):
    class Meta:
        model = ComputerHistory
        fields = ['employee']

class LocationComputerHistoryForm(EmployeeHistoryForm):
    class Meta:
        model = ComputerHistory
        fields = ['location']

class EmployeePrinterHistoryForm(EmployeeHistoryForm):
    class Meta:
        model = PrinterHistory
        fields = ['employee']

class LocationPrinterHistoryForm(EmployeeHistoryForm):
    class Meta:
        model = PrinterHistory
        fields = ['location']