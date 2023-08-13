from django.contrib import admin
from .models import (
    EquipmentCategory, Manufacturer, EquipmentStatus, Computer, 
    Employee, ComputerMovementHistory, Motherboard, Processor, 
    RAM, GraphicsCard, Storage, PowerSupply, Cooler, Case, NetworkCard,
    ComponentStatus, MemoryType
)

class ComputerAdmin(admin.ModelAdmin):
    pass

class ManufacturerAdmin(admin.ModelAdmin):
    pass

class EquipmentStatusAdmin(admin.ModelAdmin):
    pass

class EmployeeAdmin(admin.ModelAdmin):
    pass

class ComputerMovementHistoryAdmin(admin.ModelAdmin):
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

class ComonentStatusAdmin(admin.ModelAdmin):
    pass

class MemoryTypeAdmin(admin.ModelAdmin):
    pass
# Регистрируем классы в административной панели
admin.site.register(EquipmentCategory)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(EquipmentStatus, EquipmentStatusAdmin)
admin.site.register(Computer, ComputerAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(ComputerMovementHistory, ComputerMovementHistoryAdmin)
admin.site.register(Motherboard, MotherboardAdmin)
admin.site.register(Processor, ProcessorAdmin)
admin.site.register(RAM, RAMAdmin)
admin.site.register(GraphicsCard, GraphicsCardAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(PowerSupply, PowerSupplyAdmin)
admin.site.register(Cooler, CoolerAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(NetworkCard, NetworkCardAdmin)
admin.site.register(ComponentStatus, ComonentStatusAdmin)
admin.site.register(MemoryType, MemoryTypeAdmin)
