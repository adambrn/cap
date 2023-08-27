from django.contrib import admin

from cap.history.models import EquipmentHistory, ComputersHistory, PrintersHistory

# Register your models here.
class EquipmentHistoryAdmin(admin.ModelAdmin):
   pass

class ComputerHistoryAdmin(admin.ModelAdmin):
   pass

class PrinterHistoryAdmin(admin.ModelAdmin):
   pass

admin.site.register(EquipmentHistory, EquipmentHistoryAdmin)
admin.site.register(ComputersHistory, ComputerHistoryAdmin)
admin.site.register(PrintersHistory, PrinterHistoryAdmin)