from django.contrib import admin

from history.models import *

class ComputerHistoryAdmin(admin.ModelAdmin):
   pass

class PrinterHistoryAdmin(admin.ModelAdmin):
   pass

class ProcessorHistoryAdmin(admin.ModelAdmin):
   pass

class ProcessorHistoryAdmin(admin.ModelAdmin):
   pass

class NetworkCardHistoryAdmin(admin.ModelAdmin):
   pass

admin.site.register(NetworkCardHistory, NetworkCardHistoryAdmin)
admin.site.register(ComputerHistory, ComputerHistoryAdmin)
admin.site.register(PrinterHistory, PrinterHistoryAdmin)
admin.site.register(ProcessorHistory, ProcessorHistoryAdmin)