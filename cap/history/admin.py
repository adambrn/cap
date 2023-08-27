from django.contrib import admin

from history.models import  ComputersHistory, PrintersHistory

class ComputerHistoryAdmin(admin.ModelAdmin):
   pass

class PrinterHistoryAdmin(admin.ModelAdmin):
   pass

admin.site.register(ComputersHistory, ComputerHistoryAdmin)
admin.site.register(PrintersHistory, PrinterHistoryAdmin)