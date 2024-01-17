from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


class ComputerAdmin(admin.ModelAdmin):
    pass

class PrinterAdmin(admin.ModelAdmin):
    pass

class NetworkDeviceAdmin(admin.ModelAdmin):
    pass

class PhoneAdmin(admin.ModelAdmin):
    pass


class PeripheralsAdmin(admin.ModelAdmin):
    pass

# Регистрация всех моделей

admin.site.register(Computer, ComputerAdmin)  
admin.site.register(Printer, PrinterAdmin)
admin.site.register(NetworkDevice, NetworkDeviceAdmin)
admin.site.register(Phone, PhoneAdmin)


admin.site.register(Peripherals, PeripheralsAdmin)