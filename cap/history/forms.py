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

class EmployeeMonitorHistoryForm(EmployeeHistoryForm):
    class Meta:
        model = MonitorHistory
        fields = ['employee']

class LocationMonitorHistoryForm(EmployeeHistoryForm):
    class Meta:
        model = MonitorHistory
        fields = ['location']

class EmployeePhoneHistoryForm(EmployeeHistoryForm):
    class Meta:
        model = PhoneHistory
        fields = ['employee']

class LocationPhoneHistoryForm(EmployeeHistoryForm):
    class Meta:
        model = PhoneHistory
        fields = ['location']

class EmployeeNetworkDeviceHistoryForm(EmployeeHistoryForm):
    class Meta:
        model = NetworkDeviceHistory
        fields = ['employee']

class LocationNetworkDeviceHistoryForm(EmployeeHistoryForm):
    class Meta:
        model = NetworkDeviceHistory
        fields = ['location']

class EmployeeOtherEquipmentHistoryForm(EmployeeHistoryForm):
    class Meta:
        model = OtherEquipmentHistory
        fields = ['employee']

class LocationOtherEquipmentHistoryForm(EmployeeHistoryForm):
    class Meta:
        model = OtherEquipmentHistory
        fields = ['location']