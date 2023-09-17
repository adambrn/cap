from django.contrib import admin

from history.models import *

class ComputerHistoryAdmin(admin.ModelAdmin):
   pass

class PrinterHistoryAdmin(admin.ModelAdmin):
   pass

admin.site.register(ComputerHistory, ComputerHistoryAdmin)
admin.site.register(PrinterHistory, PrinterHistoryAdmin)