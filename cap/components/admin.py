from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


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


# Регистрация всех моделей
admin.site.register(Motherboard, MotherboardAdmin)
admin.site.register(Processor, ProcessorAdmin)
admin.site.register(RAM, RAMAdmin)
admin.site.register(GraphicsCard, GraphicsCardAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(PowerSupply, PowerSupplyAdmin)
admin.site.register(Cooler, CoolerAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(NetworkCard, NetworkCardAdmin)
