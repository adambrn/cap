from django.db import models
from django.urls import reverse
from django.utils import timezone

# Общие справочники
class BaseCommonInfo(models.Model):

    class Meta:
        abstract = True
        
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    
    def get_absolute_url(self):
        return reverse(f'catalogs:{self._meta.model_name}_detail', args=[str(self.id)])
    
    def get_update_url(self):
        return reverse(f'catalogs:{self._meta.model_name}_update', args=[str(self.id)])
    
    def get_delete_url(self):
        return reverse(f'catalogs:{self._meta.model_name}_delete', args=[str(self.id)])

    def __str__(self) -> str:
        return str(self.name)
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
    
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
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class Location(BaseCommonInfo):
    address = models.CharField(max_length=500, verbose_name='Адрес')
    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'
