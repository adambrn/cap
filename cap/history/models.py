from django.db import models
from catalogs.models import Employee, Location
from equipments.models import Computer, Printer
# Create your models here.
# Движение техники
class EquipmentHistory(models.Model):

    class Meta:
        abstract = True
        verbose_name = 'История оборудования'
        verbose_name_plural = 'История оборудования'

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Сотрудник')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Местоположение')
    start_date = models.DateField(null=True, blank=True, verbose_name='Дата выдачи')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата возврата')

class ComputersHistory(EquipmentHistory):
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, verbose_name='Компьютер')

class PrintersHistory(EquipmentHistory):
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE, verbose_name='Принтер')

