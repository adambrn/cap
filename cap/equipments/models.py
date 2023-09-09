from django.db import models
from catalogs.models import *
# Техника
class Equipment(models.Model):
    
    class Meta:
        abstract = True

    name = models.CharField(max_length=100, verbose_name='Название')
    category = models.ForeignKey(EquipmentCategory, on_delete=models.CASCADE, verbose_name='Категория')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name='Производитель')
    model = models.CharField(max_length=100, blank=True, null=True, verbose_name='Модель')
    serial_number = models.CharField(max_length=100, verbose_name='Серийный номер')
    inventory_number = models.CharField(max_length=100, verbose_name='Инвентарный номер')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    purchase_date = models.DateField(verbose_name='Дата приобретения')
    equipment_status = models.ForeignKey(EquipmentStatus, on_delete=models.CASCADE, verbose_name='Статус')
    
    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'

    def __str__(self) -> str:
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse(f'equipments:{self._meta.model_name}_detail', args=[str(self.id)])

class Computer(Equipment):
    class Meta:
        verbose_name = 'Компьютер'
        verbose_name_plural = 'Компьютеры'
    
class Printer(Equipment):
    class Meta:
        verbose_name = 'Принтер'
        verbose_name_plural = 'Принтеры'

class NetworkDevice(Equipment):
    class Meta:
        verbose_name = 'Сетевое устройство'
        verbose_name_plural = 'Сетевые устройства'

class Phone(Equipment):
    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

class OtherEquipment(Equipment):
    
    class Meta:
        verbose_name = 'Другое оборудование'
        verbose_name_plural = 'Другое оборудование'


# Периферия
class Peripherals(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Название')
    serial_number = models.CharField(max_length=100, verbose_name='Серийный номер') 
    inventory_number = models.CharField(max_length=100, verbose_name='Инвентарный номер')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name='Производитель')

    class Meta:
        verbose_name = 'Периферийное устройство'
        verbose_name_plural = 'Периферийные устройства'