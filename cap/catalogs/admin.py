from django.contrib import admin
from .models import (
    Manufacturer, EquipmentCategory, EquipmentStatus, ComponentStatus, 
    MemoryType, StorageType, Computer, Printer, NetworkDevice, Phone, 
    Motherboard, Processor, RAM, GraphicsCard, Storage, 
    PowerSupply, Cooler, Case, NetworkCard, 
    Employee, Location, ComputerMovementHistory,
    Peripherals
)

class ManufacturerAdmin(admin.ModelAdmin):
    pass

class EquipmentCategoryAdmin(admin.ModelAdmin):
    pass

class EquipmentStatusAdmin(admin.ModelAdmin):
    pass  

class ComponentStatusAdmin(admin.ModelAdmin):
    pass

class MemoryTypeAdmin(admin.ModelAdmin):
    pass

class StorageTypeAdmin(admin.ModelAdmin):
    pass

class ComputerAdmin(admin.ModelAdmin):
    pass

class PrinterAdmin(admin.ModelAdmin):
    pass

class NetworkDeviceAdmin(admin.ModelAdmin):
    pass

class PhoneAdmin(admin.ModelAdmin):
    pass

class MotherboardAdmin(admin.ModelAdmin):
    pass

class ProcessorAdmin(admin.ModelAdmin):
    pass

class RAMAdmin(admin.ModelAdmin):
    pass

class GraphicsCardAdmin(admin.ModelAdmin):
    pass

class StorageAdmin(admin.ModelAdmin):
    pass

class PowerSupplyAdmin(admin.ModelAdmin):
    pass

class CoolerAdmin(admin.ModelAdmin):
    pass

class CaseAdmin(admin.ModelAdmin):
    pass

class NetworkCardAdmin(admin.ModelAdmin):
    pass

class EmployeeAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass

class ComputerMovementHistoryAdmin(admin.ModelAdmin):
    pass

class PeripheralsAdmin(admin.ModelAdmin):
    pass

# Регистрация всех моделей
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(EquipmentCategory, EquipmentCategoryAdmin)
admin.site.register(EquipmentStatus, EquipmentStatusAdmin)
admin.site.register(ComponentStatus, ComponentStatusAdmin)
admin.site.register(MemoryType, MemoryTypeAdmin)
admin.site.register(StorageType, StorageTypeAdmin)
admin.site.register(Computer, ComputerAdmin)  
admin.site.register(Printer, PrinterAdmin)
admin.site.register(NetworkDevice, NetworkDeviceAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Motherboard, MotherboardAdmin)
admin.site.register(Processor, ProcessorAdmin)
admin.site.register(RAM, RAMAdmin)
admin.site.register(GraphicsCard, GraphicsCardAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(PowerSupply, PowerSupplyAdmin)
admin.site.register(Cooler, CoolerAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(NetworkCard, NetworkCardAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(ComputerMovementHistory, ComputerMovementHistoryAdmin)  
admin.site.register(Peripherals, PeripheralsAdmin)