from django.db import models
from catalogs.models import Employee, Location
from equipments.models import *
from components.models import *

# Движение техники
class EquipmentHistory(models.Model):

    class Meta:
        abstract = True
        verbose_name = 'История оборудования'
        verbose_name_plural = 'История оборудования'

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Сотрудник')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Местоположение')
    start_date = models.DateField(null=True, blank=True, verbose_name='Дата выдачи')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата возврата')

class ComputerHistory(EquipmentHistory):
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, verbose_name='Компьютер')

class MonitorHistory(EquipmentHistory):
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE, verbose_name='Монитор')

class PrinterHistory(EquipmentHistory):
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE, verbose_name='Принтер')

class PhoneHistory(EquipmentHistory):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, verbose_name='Телефон')

class NetworkDeviceHistory(EquipmentHistory):
    networkdevice = models.ForeignKey(NetworkDevice, on_delete=models.CASCADE, verbose_name='Сетевое оборудование')

class OtherEquipmentHistory(EquipmentHistory):
    otherequipment = models.ForeignKey(OtherEquipment, on_delete=models.CASCADE, verbose_name='Другое оборудование')

class ComputerComponentHistory(models.Model):

    class Meta:
        abstract = True
        verbose_name = 'История компонента'
        verbose_name_plural = 'История компонентов'

    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, verbose_name='Компьютер')
    start_date = models.DateField(null=True, blank=True, verbose_name='Дата выдачи')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата возврата')

class MotherBoardHistory(ComputerComponentHistory):
    motherboard = models.ForeignKey(Motherboard, on_delete=models.CASCADE, verbose_name='Материнская плата')

class ProcessorHistory(ComputerComponentHistory):
    processor = models.ForeignKey(Processor, on_delete=models.CASCADE, verbose_name='Процессор')

class RAMHistory(ComputerComponentHistory):
    memory = models.ForeignKey(RAM, on_delete=models.CASCADE, verbose_name='Оперативная память')

class StorageHistory(ComputerComponentHistory):
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE, verbose_name='Жесткий диск')

class GraphicsCardHistory(ComputerComponentHistory):
    graphicscard = models.ForeignKey(GraphicsCard, on_delete=models.CASCADE, verbose_name='Видеокарта')

class CoolerHistory(ComputerComponentHistory):
    cooler = models.ForeignKey(Cooler, on_delete=models.CASCADE, verbose_name='Система охлаждения')

class PowerSupplyHistory(ComputerComponentHistory):
    powersupply = models.ForeignKey(PowerSupply, on_delete=models.CASCADE, verbose_name='Блок питания')

class CaseHistory(ComputerComponentHistory):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, verbose_name='Корпус')

class NetworkCardHistory(ComputerComponentHistory):
    networkcard = models.ForeignKey(NetworkCard, on_delete=models.CASCADE, verbose_name='Сетевая карта')

class OtherComponentHistory(ComputerComponentHistory):
    othercomponent = models.ForeignKey(OtherComponent, on_delete=models.CASCADE, verbose_name='Другие компоненты')

#Подключения оборудования к компьютеру

class ComputerConnections(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, verbose_name='Компьютер')
    start_date = models.DateField(null=True, blank=True, verbose_name='Дата выдачи')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата возврата')
    connected_monitor = models.ForeignKey(Monitor, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Подключенный монитор')
    connected_printer = models.ForeignKey(Printer, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Подключенный Принтер')

