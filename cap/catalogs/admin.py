from django.contrib import admin
from .models import (
    EquipmentCategory, Manufacturer, EquipmentStatus, Equipment, 
    Employee, EquipmentMovementHistory, Motherboard, Processor, 
    RAM, GraphicsCard, Storage, PowerSupply, Cooler, Case, NetworkCard
)

class EquipmentAdmin(admin.ModelAdmin):
    pass

class ManufacturerAdmin(admin.ModelAdmin):
    pass

class EquipmentStatusAdmin(admin.ModelAdmin):
    pass

class EmployeeAdmin(admin.ModelAdmin):
    pass

class EquipmentMovementHistoryAdmin(admin.ModelAdmin):
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

# Регистрируем классы в административной панели
admin.site.register(EquipmentCategory)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(EquipmentStatus, EquipmentStatusAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EquipmentMovementHistory, EquipmentMovementHistoryAdmin)
admin.site.register(Motherboard, MotherboardAdmin)
admin.site.register(Processor, ProcessorAdmin)
admin.site.register(RAM, RAMAdmin)
admin.site.register(GraphicsCard, GraphicsCardAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(PowerSupply, PowerSupplyAdmin)
admin.site.register(Cooler, CoolerAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(NetworkCard, NetworkCardAdmin)
