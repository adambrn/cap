# python manage.py populate_sample_data
from django.core.management.base import BaseCommand
from faker import Faker
from catalogs.models import Manufacturer, EquipmentCategory, EquipmentStatus, ComponentStatus, MemoryType, StorageType
from catalogs.models import Computer, Printer, NetworkDevice, Phone, OtherEquipment
from catalogs.models import Motherboard, Processor, RAM, GraphicsCard, Storage, PowerSupply, Cooler, Case, NetworkCard, OtherComponent
from catalogs.models import Peripherals
import random

fake = Faker('ru_RU')

class Command(BaseCommand):
    help = 'Заполняет образцовые данные для компонентов, оборудования и периферии'

    def handle(self, *args, **options):
        self.populate_common_info()
        self.populate_equipment()
        self.populate_components()
        self.populate_peripherals()

    def get_random_manufacturer(self):
        return random.choice(Manufacturer.objects.all())
    def get_random_memory_type(self):
        return random.choice(MemoryType.objects.all())
    def get_random_storage_type(self):
        return random.choice(StorageType.objects.all())
    
    def populate_common_info(self):
        manufacturers = ['Asus', 'AMD', 'Nvidia', 'HP', 'Dell']
        for manufacturer in manufacturers:
            Manufacturer.objects.get_or_create(name=manufacturer)
        
        equipment_categories = ['Настольный компьютер', 'Принтер', 'Сетевое устройство', 'Телефон', 'Другое оборудование']
        for category in equipment_categories:
            EquipmentCategory.objects.get_or_create(name=category)
        
        equipment_statuses = ['Рабочее', 'Сломано', 'В ремонте', 'Списано']
        for status in equipment_statuses:
            EquipmentStatus.objects.get_or_create(name=status)
        
        component_statuses = ['Новый', 'Б/У']
        for status in component_statuses:
            ComponentStatus.objects.get_or_create(name=status)
        
        memory_types = ['DDR3', 'DDR4', 'DDR5']
        for memory_type in memory_types:
            MemoryType.objects.get_or_create(name=memory_type)
        
        storage_types = ['HDD', 'SSD', 'NVMe']
        for storage_type in storage_types:
            StorageType.objects.get_or_create(name=storage_type)

    def populate_equipment(self):
        for _ in range(10):
            name = fake.word()
            category = EquipmentCategory.objects.get(name='Настольный компьютер')
            manufacturer = self.get_random_manufacturer()
            serial_number = fake.random_int(min=100000, max=999999)
            inventory_number = fake.random_int(min=10000, max=99999)
            cost = fake.pydecimal(left_digits=6, right_digits=2, positive=True)
            purchase_date = fake.date_this_decade()
            equipment_status = EquipmentStatus.objects.get(name='Рабочее')

            Computer.objects.get_or_create(
                name=name,
                category=category,
                manufacturer=manufacturer,
                serial_number=serial_number,
                inventory_number=inventory_number,
                cost=cost,
                purchase_date=purchase_date,
                equipment_status=equipment_status
            )

    def populate_components(self):
        for _ in range(10):
            name = fake.word()
            manufacturer = self.get_random_manufacturer()
            serial_number = fake.random_int(min=100000, max=999999)
            inventory_number = fake.random_int(min=10000, max=99999)
            cost = fake.pydecimal(left_digits=6, right_digits=2, positive=True)
            start_date = fake.date_this_decade()
            end_date = fake.date_this_decade()
            component_status = ComponentStatus.objects.get(name='Новый')

            Motherboard.objects.get_or_create(
                name=name,
                serial_number=serial_number,
                inventory_number=inventory_number,
                manufacturer=manufacturer,
                cost=cost,
                start_date=start_date,
                end_date=end_date,
                component_status=component_status,
                socket_type=fake.word(),
                in_computer=None
            )

            Processor.objects.get_or_create(
                name=name,
                serial_number=serial_number,
                inventory_number=inventory_number,
                manufacturer=manufacturer,
                cost=cost,
                start_date=start_date,
                end_date=end_date,
                component_status=component_status,
                num_cores=fake.random_int(min=2, max=8),
                frequency=fake.random_int(min=1000, max=5000),
                in_computer=None
            )

            RAM.objects.get_or_create(
                name=name,
                serial_number=serial_number,
                inventory_number=inventory_number,
                manufacturer=manufacturer,
                cost=cost,
                start_date=start_date,
                end_date=end_date,
                component_status=component_status,
                memory_type=self.get_random_memory_type(),
                capacity=fake.random_int(min=4, max=64),
                frequency=fake.random_int(min=1600, max=4000),
                in_computer=None
            )

            GraphicsCard.objects.get_or_create(
                name=name,
                serial_number=serial_number,
                inventory_number=inventory_number,
                manufacturer=manufacturer,
                cost=cost,
                start_date=start_date,
                end_date=end_date,
                component_status=component_status,
                memory=fake.word(),
                frequency=fake.random_int(min=1000, max=2000),
                in_computer=None
            )

            Storage.objects.get_or_create(
                name=name,
                serial_number=serial_number,
                inventory_number=inventory_number,
                manufacturer=manufacturer,
                cost=cost,
                start_date=start_date,
                end_date=end_date,
                component_status=component_status,
                storage_type=self.get_random_storage_type(),
                capacity=fake.random_int(min=128, max=4096),
                interface=fake.word(),
                in_computer=None
            )

            PowerSupply.objects.get_or_create(
                name=name,
                serial_number=serial_number,
                inventory_number=inventory_number,
                manufacturer=manufacturer,
                cost=cost,
                start_date=start_date,
                end_date=end_date,
                component_status=component_status,
                power=fake.random_int(min=300, max=1000),
                in_computer=None
            )

            Cooler.objects.get_or_create(
                name=name,
                serial_number=serial_number,
                inventory_number=inventory_number,
                manufacturer=manufacturer,
                cost=cost,
                start_date=start_date,
                end_date=end_date,
                component_status=component_status,
                cooler_type=fake.word(),
                size=fake.word(),
                in_computer=None
            )

            Case.objects.get_or_create(
                name=name,
                serial_number=serial_number,
                inventory_number=inventory_number,
                manufacturer=manufacturer,
                cost=cost,
                start_date=start_date,
                end_date=end_date,
                component_status=component_status,
                case_type=fake.word(),
                num_bays=fake.random_int(min=1, max=5),
                in_computer=None
            )

            NetworkCard.objects.get_or_create(
                name=name,
                serial_number=serial_number,
                inventory_number=inventory_number,
                manufacturer=manufacturer,
                cost=cost,
                start_date=start_date,
                end_date=end_date,
                component_status=component_status,
                speed=fake.word(),
                card_type=fake.word(),
                in_computer=None
            )

            OtherComponent.objects.get_or_create(
                name=name,
                serial_number=serial_number,
                inventory_number=inventory_number,
                manufacturer=manufacturer,
                cost=cost,
                start_date=start_date,
                end_date=end_date,
                component_status=component_status
            )


    def populate_peripherals(self):
        for _ in range(10):
            name = fake.word()
            manufacturer = self.get_random_manufacturer()
            serial_number = fake.random_int(min=100000, max=999999)
            inventory_number = fake.random_int(min=10000, max=99999)

            Peripherals.objects.get_or_create(
                name=name,
                manufacturer=manufacturer,
                serial_number=serial_number,
                inventory_number=inventory_number
            )
