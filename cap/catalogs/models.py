from django.db import models
from django.urls import reverse

class BaseCommonInfo(models.Model):

    class Meta:
        abstract = True

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)
    
class Manufacturer(BaseCommonInfo):
    pass

class EquipmentCategory(BaseCommonInfo):
    pass

class EquipmentStatus(BaseCommonInfo):
    pass

class ComponentStatus(BaseCommonInfo):
    pass

class MemoryType(BaseCommonInfo):
    pass

class StorageType(BaseCommonInfo):
    pass

class Equipment(models.Model):

    class Meta:
        abstract = True

    name = models.CharField(max_length=100)
    category = models.ForeignKey(EquipmentCategory, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.CharField(max_length=100, blank=True, null=True)
    serial_number = models.CharField(max_length=100)
    inventory_number = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()
    equipment_status = models.ForeignKey(EquipmentStatus, on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return str(self.name)

    
class Employee(BaseCommonInfo):
    position = models.CharField(max_length=100)

class Location(BaseCommonInfo):
    address = models.CharField(max_length=500)

class ComputerMovementHistory(models.Model):
    equipment = models.ForeignKey('Computer', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    issue_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

class BaseComponent(models.Model):

    class Meta:
        abstract = True

    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100) 
    inventory_number = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    component_status = models.ForeignKey(ComponentStatus, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('catalogs:component_detail', args=[self._meta.model_name, str(self.id)])
    
    def __str__(self) -> str:
        return str(self.name)

class Computer(Equipment):
    
    pass

class Motherboard(BaseComponent):
    socket_type = models.CharField(max_length=50)
    supported_memory_types = models.ManyToManyField(MemoryType)
    in_computer = models.OneToOneField(Computer, on_delete=models.SET_NULL,blank=True, null=True)

class Processor(BaseComponent):
    num_cores = models.IntegerField()
    frequency = models.IntegerField()
    in_computer = models.ForeignKey(Computer, on_delete=models.SET_NULL,blank=True, null=True)

class RAM(BaseComponent):
    memory_type = models.ForeignKey(MemoryType,on_delete=models.SET_NULL, blank=True, null=True)
    capacity = models.IntegerField()
    frequency = models.IntegerField()
    in_computer = models.ForeignKey(Computer, on_delete=models.SET_NULL, blank=True, null=True)

class GraphicsCard(BaseComponent):
    memory = models.CharField(max_length=20)
    frequency = models.IntegerField()
    in_computer = models.ForeignKey(Computer, on_delete=models.SET_NULL,blank=True, null=True)

class Storage(BaseComponent):
    storage_type = models.ForeignKey(StorageType, on_delete=models.DO_NOTHING)
    capacity = models.IntegerField()
    interface = models.CharField(max_length=50)
    in_computer = models.ForeignKey(Computer, on_delete=models.SET_NULL,blank=True, null=True)

class PowerSupply(BaseComponent):
    power = models.IntegerField()
    in_computer = models.ForeignKey(Computer, on_delete=models.SET_NULL,blank=True, null=True)

class Cooler(BaseComponent):
    cooler_type = models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    in_computer = models.ForeignKey(Computer, on_delete=models.SET_NULL,blank=True, null=True)

class Case(BaseComponent):
    case_type = models.CharField(max_length=50)
    num_bays = models.IntegerField()
    in_computer = models.ForeignKey(Computer, on_delete=models.SET_NULL,blank=True, null=True)

class NetworkCard(BaseComponent):
    speed = models.CharField(max_length=20)
    card_type = models.CharField(max_length=50)
    in_computer = models.ForeignKey(Computer, on_delete=models.SET_NULL,blank=True, null=True)

