from django.db import models
from catalogs.models import *
from equipments.models import *

# Компоненты компьютера
class BaseComponent(models.Model):

    class Meta:
        abstract = True
        verbose_name = 'Компоненты оборудования'
        verbose_name_plural = 'Компоненты оборудования'

    name = models.CharField(max_length=100, verbose_name='Название')
    serial_number = models.CharField(max_length=100, verbose_name='Серийный номер') 
    inventory_number = models.CharField(max_length=100, verbose_name='Инвентарный номер')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, verbose_name='Производитель')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    start_date = models.DateField(verbose_name='Дата начала использования')
    end_date = models.DateField(blank=True, null=True, verbose_name='Дата окончания использования')
    component_status = models.ForeignKey(ComponentStatus, on_delete=models.SET_NULL, null=True, verbose_name='Статус')
    
    def get_absolute_url(self):
        return reverse(f'components:{self._meta.model_name}_detail', kwargs={"pk": self.pk})
    
    def get_model_fields(self):
        fields = []
        for field in self._meta.get_fields():
            if "ptr" not in field.name:
                if hasattr(field, 'verbose_name'):
                    fields.append({"label": field.verbose_name, "value": getattr(self, field.name)})
        return fields
              
    def __str__(self) -> str:
        return str(self.name)

class Motherboard(BaseComponent):
    socket_type = models.ForeignKey(SocketType, on_delete=models.SET_NULL, null=True, verbose_name='Сокет')
    supported_memory_types = models.ManyToManyField(MemoryType, verbose_name='Поддерживаемые типы памяти')
    in_computer = models.OneToOneField(Computer, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Компьютер')

    class Meta:
        verbose_name = 'Материнская плата'
        verbose_name_plural = 'Материнские платы'

class Processor(BaseComponent):
    socket_type = models.ForeignKey(SocketType, on_delete=models.SET_NULL, null=True, verbose_name='Сокет')
    num_cores = models.IntegerField(verbose_name='Количество ядер')
    frequency = models.IntegerField(verbose_name='Частота')
    in_computer = models.ForeignKey(Computer, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Компьютер')

    class Meta:
        verbose_name = 'Процессор'
        verbose_name_plural = 'Процессоры'

class RAM(BaseComponent):
    memory_type = models.ForeignKey(MemoryType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Тип памяти')
    capacity = models.IntegerField(verbose_name='Объем')
    frequency = models.IntegerField(verbose_name='Частота')
    in_computer = models.ForeignKey(Computer, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Компьютер')
    
    class Meta:
        verbose_name = 'Оперативная память'
        verbose_name_plural = 'Оперативная память'

class GraphicsCard(BaseComponent):
    memory = models.CharField(max_length=20, verbose_name='Объем памяти')
    frequency = models.IntegerField(verbose_name='Частота')
    in_computer = models.ForeignKey(Computer, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Компьютер')

    class Meta:
        verbose_name = 'Видеокарта'
        verbose_name_plural = 'Видеокарты'

class Storage(BaseComponent):
    storage_type = models.ForeignKey(StorageType, on_delete=models.DO_NOTHING, verbose_name='Тип хранения')
    capacity = models.IntegerField(verbose_name='Объем')
    interface = models.CharField(max_length=50, verbose_name='Интерфейс')
    in_computer = models.ForeignKey(Computer, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Компьютер')
    class Meta:
        verbose_name = 'Накопитель'
        verbose_name_plural = 'Накопители'

class PowerSupply(BaseComponent):
    power = models.IntegerField(verbose_name='Мощность')
    in_computer = models.ForeignKey(Computer, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Компьютер')

    class Meta:
        verbose_name = 'Блок питания'
        verbose_name_plural = 'Блоки питания'

class Cooler(BaseComponent):
    cooler_type = models.CharField(max_length=50, verbose_name='Тип кулера')
    size = models.CharField(max_length=20, verbose_name='Размер')
    in_computer = models.ForeignKey(Computer, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Компьютер')

    class Meta:
        verbose_name = 'Система охлаждения'
        verbose_name_plural = 'Системы охлаждения'

class Case(BaseComponent):
    case_type = models.CharField(max_length=50, verbose_name='Тип корпуса')
    num_bays = models.IntegerField(verbose_name='Количество отсеков')
    in_computer = models.ForeignKey(Computer, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Компьютер')

    class Meta:
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпуса'

class NetworkCard(BaseComponent):
    speed = models.CharField(max_length=20, verbose_name='Скорость')
    card_type = models.CharField(max_length=50, verbose_name='Тип сетевой карты')
    in_computer = models.ForeignKey(Computer, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Компьютер')

    class Meta:
        verbose_name = 'Сетевая карта'
        verbose_name_plural = 'Сетевые карты'

class OtherComponent(BaseComponent):
    class Meta:
        verbose_name = 'Другой компонент'
        verbose_name_plural = 'Другие компоненты'

