from django.contrib import admin
from .models import *

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

class EmployeeAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass

# Регистрация всех моделей
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(EquipmentCategory, EquipmentCategoryAdmin)
admin.site.register(EquipmentStatus, EquipmentStatusAdmin)
admin.site.register(ComponentStatus, ComponentStatusAdmin)
admin.site.register(MemoryType, MemoryTypeAdmin)
admin.site.register(StorageType, StorageTypeAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Location, LocationAdmin)
