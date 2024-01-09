# Generated by Django 4.2.4 on 2024-01-09 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('components', '0001_initial'),
        ('equipments', '0001_initial'),
        ('catalogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StorageHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата возврата')),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.computer', verbose_name='Компьютер')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.storage', verbose_name='Жесткий диск')),
            ],
            options={
                'verbose_name': 'История компонента',
                'verbose_name_plural': 'История компонентов',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RAMHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата возврата')),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.computer', verbose_name='Компьютер')),
                ('memory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.ram', verbose_name='Оперативная память')),
            ],
            options={
                'verbose_name': 'История компонента',
                'verbose_name_plural': 'История компонентов',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProcessorHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата возврата')),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.computer', verbose_name='Компьютер')),
                ('processor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.processor', verbose_name='Процессор')),
            ],
            options={
                'verbose_name': 'История компонента',
                'verbose_name_plural': 'История компонентов',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PrinterHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата возврата')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogs.employee', verbose_name='Сотрудник')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogs.location', verbose_name='Местоположение')),
                ('printer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.printer', verbose_name='Принтер')),
            ],
            options={
                'verbose_name': 'История оборудования',
                'verbose_name_plural': 'История оборудования',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PowerSupplyHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата возврата')),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.computer', verbose_name='Компьютер')),
                ('powersupply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.powersupply', verbose_name='Блок питания')),
            ],
            options={
                'verbose_name': 'История компонента',
                'verbose_name_plural': 'История компонентов',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PhoneHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата возврата')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogs.employee', verbose_name='Сотрудник')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogs.location', verbose_name='Местоположение')),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.phone', verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'История оборудования',
                'verbose_name_plural': 'История оборудования',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OtherEquipmentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата возврата')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogs.employee', verbose_name='Сотрудник')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogs.location', verbose_name='Местоположение')),
                ('otherequipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.otherequipment', verbose_name='Другое оборудование')),
            ],
            options={
                'verbose_name': 'История оборудования',
                'verbose_name_plural': 'История оборудования',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OtherComponentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата возврата')),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.computer', verbose_name='Компьютер')),
                ('othercomponent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.othercomponent', verbose_name='Другие компоненты')),
            ],
            options={
                'verbose_name': 'История компонента',
                'verbose_name_plural': 'История компонентов',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NetworkDeviceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата возврата')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogs.employee', verbose_name='Сотрудник')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogs.location', verbose_name='Местоположение')),
                ('networkdevice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.networkdevice', verbose_name='Сетевое оборудование')),
            ],
            options={
                'verbose_name': 'История оборудования',
                'verbose_name_plural': 'История оборудования',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NetworkCardHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата возврата')),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.computer', verbose_name='Компьютер')),
                ('networkcard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.networkcard', verbose_name='Сетевая карта')),
            ],
            options={
                'verbose_name': 'История компонента',
                'verbose_name_plural': 'История компонентов',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MotherBoardHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата возврата')),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.computer', verbose_name='Компьютер')),
                ('motherboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.motherboard', verbose_name='Материнская плата')),
            ],
            options={
                'verbose_name': 'История компонента',
                'verbose_name_plural': 'История компонентов',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MonitorHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата возврата')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogs.employee', verbose_name='Сотрудник')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogs.location', verbose_name='Местоположение')),
                ('monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.monitor', verbose_name='Монитор')),
            ],
            options={
                'verbose_name': 'История оборудования',
                'verbose_name_plural': 'История оборудования',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GraphicsCardHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата возврата')),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.computer', verbose_name='Компьютер')),
                ('graphicscard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.graphicscard', verbose_name='Видеокарта')),
            ],
            options={
                'verbose_name': 'История компонента',
                'verbose_name_plural': 'История компонентов',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CoolerHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата возврата')),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.computer', verbose_name='Компьютер')),
                ('cooler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.cooler', verbose_name='Система охлаждения')),
            ],
            options={
                'verbose_name': 'История компонента',
                'verbose_name_plural': 'История компонентов',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ComputerHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата возврата')),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.computer', verbose_name='Компьютер')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogs.employee', verbose_name='Сотрудник')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogs.location', verbose_name='Местоположение')),
            ],
            options={
                'verbose_name': 'История оборудования',
                'verbose_name_plural': 'История оборудования',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ComputerConnections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата возврата')),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.computer', verbose_name='Компьютер')),
                ('connected_monitor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='equipments.monitor', verbose_name='Подключенный монитор')),
                ('connected_printer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='equipments.printer', verbose_name='Подключенный Принтер')),
            ],
        ),
        migrations.CreateModel(
            name='CaseHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата возврата')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.case', verbose_name='Корпус')),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.computer', verbose_name='Компьютер')),
            ],
            options={
                'verbose_name': 'История компонента',
                'verbose_name_plural': 'История компонентов',
                'abstract': False,
            },
        ),
    ]
