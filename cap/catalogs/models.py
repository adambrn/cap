from django.db import models
from django.urls import reverse

# Общие справочники
class BaseCommonInfo(models.Model):

    class Meta:
        abstract = True
        
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self) -> str:
        return str(self.name)
    
class Manufacturer(BaseCommonInfo):
    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

class EquipmentCategory(BaseCommonInfo):
    class Meta:
        verbose_name = 'Категория оборудования'
        verbose_name_plural = 'Категории оборудования'

class EquipmentStatus(BaseCommonInfo):
    class Meta:
        verbose_name = 'Статус оборудования'
        verbose_name_plural = 'Статусы оборудования'

class ComponentStatus(BaseCommonInfo):
    class Meta:
        verbose_name = 'Статус компонента'
        verbose_name_plural = 'Статусы компонентов'

class MemoryType(BaseCommonInfo):
    class Meta:
        verbose_name = 'Тип памяти'
        verbose_name_plural = 'Типы памяти'

class StorageType(BaseCommonInfo):
    class Meta:
        verbose_name = 'Тип хранения'
        verbose_name_plural = 'Типы хранения'

class SocketType(BaseCommonInfo):
    class Meta:
        verbose_name = 'Тип сокета'
        verbose_name_plural = 'Типы сокетов'

# Принадлежность техники
class Employee(BaseCommonInfo):
    position = models.CharField(max_length=100, verbose_name='Должность')

class Location(BaseCommonInfo):
    address = models.CharField(max_length=500, verbose_name='Адрес')
