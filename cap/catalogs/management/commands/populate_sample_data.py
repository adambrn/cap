# python manage.py populate_sample_data
import random
from django.core.management.base import BaseCommand
from faker import Faker
from catalogs.models import *
from components.models import *
from equipments.models import *

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
    def get_random_socket_type(self):
        return random.choice(SocketType.objects.all())
    
    
    
    def populate_common_info(self):
        manufacturers = ['Asus', 'AMD', 'Nvidia', 'HP', 'Dell', 'Intel', 'AsRock', 'MSI', 'AFox', 'Kyocera']
        for manufacturer in manufacturers:
            Manufacturer.objects.get_or_create(name=manufacturer)
        
        equipment_categories = ['Настольный компьютер', 'Монитор', 'Принтер', 'Сетевое устройство', 'Телефон', 'Другое оборудование']
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
        
        socket_types = ['AM4', 'AM3', 'AM2','FM1', 'FM2','775', '1200', '1155', '1156']
        for socket_type in socket_types:
            SocketType.objects.get_or_create(name=socket_type)

        employees = ['Иван', 'Марья', 'Семён Семёнович']
        for employee in employees:
            Employee.objects.get_or_create(name=employee, position=fake.job())

        locations = ['Серверная', 'Склад', 'Кабинет1']
        for location in locations:
            Location.objects.get_or_create(name=location)

    def populate_equipment(self):
        for i in range(10):
            Computer.objects.get_or_create(
                name = f'Компьютер № {i}',
                category = EquipmentCategory.objects.get(name='Настольный компьютер'),
                manufacturer = self.get_random_manufacturer(),
                serial_number = fake.random_int(min=100000, max=999999),
                inventory_number = fake.random_int(min=10000, max=99999),
                cost = fake.pydecimal(left_digits=6, right_digits=2, positive=True),
                purchase_date = fake.date_time(),
                equipment_status = EquipmentStatus.objects.get(name='Рабочее'),
            )
            Monitor.objects.get_or_create(
                name = f'Монитор № {i}',
                category = EquipmentCategory.objects.get(name='Монитор'),
                manufacturer = self.get_random_manufacturer(),
                serial_number = fake.random_int(min=100000, max=999999),
                inventory_number = fake.random_int(min=10000, max=99999),
                cost = fake.pydecimal(left_digits=6, right_digits=2, positive=True),
                purchase_date = fake.date_time(),
                equipment_status = EquipmentStatus.objects.get(name='Рабочее'),
            )
            Printer.objects.get_or_create(
                name = f'Принтер № {i}',
                category = EquipmentCategory.objects.get(name='Принтер'),
                manufacturer = self.get_random_manufacturer(),
                serial_number = fake.random_int(min=100000, max=999999),
                inventory_number = fake.random_int(min=10000, max=99999),
                cost = fake.pydecimal(left_digits=6, right_digits=2, positive=True),
                purchase_date = fake.date_time(),
                equipment_status = EquipmentStatus.objects.get(name='Рабочее'),
            )

            Phone.objects.get_or_create(
                name = f'Телефон № {i}',
                category = EquipmentCategory.objects.get(name='Телефон'),
                manufacturer = self.get_random_manufacturer(),
                serial_number = fake.random_int(min=100000, max=999999),
                inventory_number = fake.random_int(min=10000, max=99999),
                cost = fake.pydecimal(left_digits=6, right_digits=2, positive=True),
                purchase_date = fake.date_time(),
                equipment_status = EquipmentStatus.objects.get(name='Рабочее'),
            )

    def populate_components(self):
        for i in range(10): 
            computer_name = f'Компьютер № {i}'
            computer = Computer.objects.filter(name=computer_name)[0]
            Motherboard.objects.get_or_create(
                name = f'Материнская плата № {i}',
                manufacturer = self.get_random_manufacturer(),
                serial_number = fake.random_int(min=100000, max=999999),
                inventory_number = fake.random_int(min=10000, max=99999),
                cost = fake.pydecimal(left_digits=6, right_digits=2, positive=True),
                start_date = fake.date_time(),
                component_status = ComponentStatus.objects.get(name='Новый'),
                socket_type=self.get_random_socket_type(),
                in_computer=computer,
            )

            Processor.objects.get_or_create(
                name = f'Процессор № {i}',
                manufacturer = self.get_random_manufacturer(),
                serial_number = fake.random_int(min=100000, max=999999),
                inventory_number = fake.random_int(min=10000, max=99999),
                cost = fake.pydecimal(left_digits=6, right_digits=2, positive=True),
                start_date = fake.date_time(),
                component_status = ComponentStatus.objects.get(name='Новый'),
                socket_type=self.get_random_socket_type(),
                num_cores=fake.random_int(min=2, max=8),
                frequency=fake.random_int(min=1000, max=5000),
                in_computer=computer,
            )

            RAM.objects.get_or_create(
                name = f'Память № {i}',
                manufacturer = self.get_random_manufacturer(),
                serial_number = fake.random_int(min=100000, max=999999),
                inventory_number = fake.random_int(min=10000, max=99999),
                cost = fake.pydecimal(left_digits=6, right_digits=2, positive=True),
                start_date = fake.date_time(),
                component_status = ComponentStatus.objects.get(name='Новый'),
                memory_type=self.get_random_memory_type(),
                capacity=fake.random_int(min=4, max=64),
                frequency=fake.random_int(min=1600, max=4000),
                in_computer=computer,
            )

            GraphicsCard.objects.get_or_create(
                name = f'Видеокарта № {i}',
                manufacturer = self.get_random_manufacturer(),
                serial_number = fake.random_int(min=100000, max=999999),
                inventory_number = fake.random_int(min=10000, max=99999),
                cost = fake.pydecimal(left_digits=6, right_digits=2, positive=True),
                start_date = fake.date_time(),
                component_status = ComponentStatus.objects.get(name='Новый'),
                memory=fake.word(),
                frequency=fake.random_int(min=1000, max=2000),
                in_computer=computer,
            )

            Storage.objects.get_or_create(
                name = f'Накопитель № {i}',
                manufacturer = self.get_random_manufacturer(),
                serial_number = fake.random_int(min=100000, max=999999),
                inventory_number = fake.random_int(min=10000, max=99999),
                cost = fake.pydecimal(left_digits=6, right_digits=2, positive=True),
                start_date = fake.date_time(),
                component_status = ComponentStatus.objects.get(name='Новый'),
                storage_type=self.get_random_storage_type(),
                capacity=fake.random_int(min=128, max=4096),
                interface='SATA3',
                in_computer=computer,
            )

            PowerSupply.objects.get_or_create(
                name = f'Блок питания № {i}',
                manufacturer = self.get_random_manufacturer(),
                serial_number = fake.random_int(min=100000, max=999999),
                inventory_number = fake.random_int(min=10000, max=99999),
                cost = fake.pydecimal(left_digits=6, right_digits=2, positive=True),
                start_date = fake.date_time(),
                component_status = ComponentStatus.objects.get(name='Новый'),
                power=fake.random_int(min=300, max=1000),
                in_computer=computer,
            )

            Cooler.objects.get_or_create(
                name = f'Куллер № {i}',
                manufacturer = self.get_random_manufacturer(),
                serial_number = fake.random_int(min=100000, max=999999),
                inventory_number = fake.random_int(min=10000, max=99999),
                cost = fake.pydecimal(left_digits=6, right_digits=2, positive=True),
                start_date = fake.date_time(),
                component_status = ComponentStatus.objects.get(name='Новый'),
                cooler_type='Процессорный',
                size="90X90",
                in_computer=computer,
            )

            Case.objects.get_or_create(
                name = f'Корпус № {i}',
                manufacturer = self.get_random_manufacturer(),
                serial_number = fake.random_int(min=100000, max=999999),
                inventory_number = fake.random_int(min=10000, max=99999),
                cost = fake.pydecimal(left_digits=6, right_digits=2, positive=True),
                start_date = fake.date_time(),
                component_status = ComponentStatus.objects.get(name='Новый'),
                case_type='ATX',
                num_bays=fake.random_int(min=1, max=5),
                in_computer=computer,
            )

            NetworkCard.objects.get_or_create(
                name = f'Сетевая карта № {i}',
                manufacturer = self.get_random_manufacturer(),
                serial_number = fake.random_int(min=100000, max=999999),
                inventory_number = fake.random_int(min=10000, max=99999),
                cost = fake.pydecimal(left_digits=6, right_digits=2, positive=True),
                start_date = fake.date_time(),
                component_status = ComponentStatus.objects.get(name='Новый'),
                speed= '10000',
                card_type='PCI-E',
                in_computer=computer,
            )

            OtherComponent.objects.get_or_create(
                name = f'Какие то еще компоненты  № {i}',
                manufacturer = self.get_random_manufacturer(),
                serial_number = fake.random_int(min=100000, max=999999),
                inventory_number = fake.random_int(min=10000, max=99999),
                cost = fake.pydecimal(left_digits=6, right_digits=2, positive=True),
                start_date = fake.date_time(),
                in_computer=computer,
            )


    def populate_peripherals(self):
        for i in range(5):
            name = f'Клавиатура № {i}'
            manufacturer = self.get_random_manufacturer()
            serial_number = fake.random_int(min=100000, max=999999)
            inventory_number = fake.random_int(min=10000, max=99999)

            Peripherals.objects.get_or_create(
                name=name,
                manufacturer=manufacturer,
                serial_number=serial_number,
                inventory_number=inventory_number
            )
