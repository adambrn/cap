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
        return reverse(f'catalogs:{self._meta.model_name}_detail', args=[str(self.id)])

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

# Принадлежность техники
class Employee(BaseCommonInfo):
    position = models.CharField(max_length=100, verbose_name='Должность')

class Location(BaseCommonInfo):
    address = models.CharField(max_length=500, verbose_name='Адрес')


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
        return reverse(f'catalogs:{self._meta.model_name}_detail', kwargs={"pk": self.pk})
    
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
