from django.db import models

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


class Equipment(models.Model):
    category = models.ForeignKey(EquipmentCategory, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()
    status = models.ForeignKey(EquipmentStatus, on_delete=models.CASCADE)
    components = models.ManyToManyField('BaseComponent', blank=True, related_name='components_relay')

class Employee(BaseCommonInfo):
    position = models.CharField(max_length=100)

class EquipmentMovementHistory(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

class BaseComponent(models.Model):

    class Meta:
        pass
        #abstract = True

    name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    status = models.ForeignKey(EquipmentStatus, on_delete=models.CASCADE)
    in_equipment = models.OneToOneField(Equipment, on_delete=models.CASCADE,blank=True, null=True, related_name='equipment_relay')

    def __str__(self) -> str:
        return str(self.name)

class Motherboard(BaseComponent):
    socket_type = models.CharField(max_length=50)
    supported_memory_types = models.CharField(max_length=100)

class Processor(BaseComponent):
    num_cores = models.IntegerField()
    frequency = models.DecimalField(max_digits=5, decimal_places=2)
    cache_size = models.CharField(max_length=50)

class RAM(BaseComponent):
    memory_type = models.CharField(max_length=50)
    capacity = models.CharField(max_length=20)
    frequency = models.DecimalField(max_digits=5, decimal_places=2)

class GraphicsCard(BaseComponent):
    memory = models.CharField(max_length=20)
    core_frequency = models.DecimalField(max_digits=5, decimal_places=2)

class Storage(BaseComponent):
    storage_type = models.CharField(max_length=50)
    capacity = models.CharField(max_length=20)
    interface = models.CharField(max_length=50)

class PowerSupply(BaseComponent):
    power = models.IntegerField()

class Cooler(BaseComponent):
    cooler_type = models.CharField(max_length=50)
    size = models.CharField(max_length=20)

class Case(BaseComponent):
    case_type = models.CharField(max_length=50)
    num_bays = models.IntegerField()

class NetworkCard(BaseComponent):
    speed = models.CharField(max_length=20)
    card_type = models.CharField(max_length=50)
