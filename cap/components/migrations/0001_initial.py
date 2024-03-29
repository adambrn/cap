# Generated by Django 4.2.4 on 2024-01-13 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("equipments", "0001_initial"),
        ("catalogs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Storage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "serial_number",
                    models.CharField(max_length=100, verbose_name="Серийный номер"),
                ),
                (
                    "inventory_number",
                    models.CharField(max_length=100, verbose_name="Инвентарный номер"),
                ),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Стоимость"
                    ),
                ),
                (
                    "start_date",
                    models.DateTimeField(verbose_name="Дата начала использования"),
                ),
                (
                    "end_date",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="Дата окончания использования",
                    ),
                ),
                ("capacity", models.IntegerField(verbose_name="Объем")),
                (
                    "interface",
                    models.CharField(max_length=50, verbose_name="Интерфейс"),
                ),
                (
                    "component_status",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.componentstatus",
                        verbose_name="Статус",
                    ),
                ),
                (
                    "in_computer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="equipments.computer",
                        verbose_name="Компьютер",
                    ),
                ),
                (
                    "manufacturer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.manufacturer",
                        verbose_name="Производитель",
                    ),
                ),
                (
                    "storage_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="catalogs.storagetype",
                        verbose_name="Тип хранения",
                    ),
                ),
            ],
            options={
                "verbose_name": "Накопитель",
                "verbose_name_plural": "Накопители",
            },
        ),
        migrations.CreateModel(
            name="RAM",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "serial_number",
                    models.CharField(max_length=100, verbose_name="Серийный номер"),
                ),
                (
                    "inventory_number",
                    models.CharField(max_length=100, verbose_name="Инвентарный номер"),
                ),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Стоимость"
                    ),
                ),
                (
                    "start_date",
                    models.DateTimeField(verbose_name="Дата начала использования"),
                ),
                (
                    "end_date",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="Дата окончания использования",
                    ),
                ),
                ("capacity", models.IntegerField(verbose_name="Объем")),
                ("frequency", models.IntegerField(verbose_name="Частота")),
                (
                    "component_status",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.componentstatus",
                        verbose_name="Статус",
                    ),
                ),
                (
                    "in_computer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="equipments.computer",
                        verbose_name="Компьютер",
                    ),
                ),
                (
                    "manufacturer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.manufacturer",
                        verbose_name="Производитель",
                    ),
                ),
                (
                    "memory_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.memorytype",
                        verbose_name="Тип памяти",
                    ),
                ),
            ],
            options={
                "verbose_name": "Оперативная память",
                "verbose_name_plural": "Оперативная память",
            },
        ),
        migrations.CreateModel(
            name="Processor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "serial_number",
                    models.CharField(max_length=100, verbose_name="Серийный номер"),
                ),
                (
                    "inventory_number",
                    models.CharField(max_length=100, verbose_name="Инвентарный номер"),
                ),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Стоимость"
                    ),
                ),
                (
                    "start_date",
                    models.DateTimeField(verbose_name="Дата начала использования"),
                ),
                (
                    "end_date",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="Дата окончания использования",
                    ),
                ),
                ("num_cores", models.IntegerField(verbose_name="Количество ядер")),
                ("frequency", models.IntegerField(verbose_name="Частота")),
                (
                    "component_status",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.componentstatus",
                        verbose_name="Статус",
                    ),
                ),
                (
                    "in_computer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="equipments.computer",
                        verbose_name="Компьютер",
                    ),
                ),
                (
                    "manufacturer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.manufacturer",
                        verbose_name="Производитель",
                    ),
                ),
                (
                    "socket_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.sockettype",
                        verbose_name="Сокет",
                    ),
                ),
            ],
            options={
                "verbose_name": "Процессор",
                "verbose_name_plural": "Процессоры",
            },
        ),
        migrations.CreateModel(
            name="PowerSupply",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "serial_number",
                    models.CharField(max_length=100, verbose_name="Серийный номер"),
                ),
                (
                    "inventory_number",
                    models.CharField(max_length=100, verbose_name="Инвентарный номер"),
                ),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Стоимость"
                    ),
                ),
                (
                    "start_date",
                    models.DateTimeField(verbose_name="Дата начала использования"),
                ),
                (
                    "end_date",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="Дата окончания использования",
                    ),
                ),
                ("power", models.IntegerField(verbose_name="Мощность")),
                (
                    "component_status",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.componentstatus",
                        verbose_name="Статус",
                    ),
                ),
                (
                    "in_computer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="equipments.computer",
                        verbose_name="Компьютер",
                    ),
                ),
                (
                    "manufacturer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.manufacturer",
                        verbose_name="Производитель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Блок питания",
                "verbose_name_plural": "Блоки питания",
            },
        ),
        migrations.CreateModel(
            name="OtherComponent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "serial_number",
                    models.CharField(max_length=100, verbose_name="Серийный номер"),
                ),
                (
                    "inventory_number",
                    models.CharField(max_length=100, verbose_name="Инвентарный номер"),
                ),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Стоимость"
                    ),
                ),
                (
                    "start_date",
                    models.DateTimeField(verbose_name="Дата начала использования"),
                ),
                (
                    "end_date",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="Дата окончания использования",
                    ),
                ),
                (
                    "component_status",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.componentstatus",
                        verbose_name="Статус",
                    ),
                ),
                (
                    "in_computer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="equipments.computer",
                        verbose_name="Компьютер",
                    ),
                ),
                (
                    "manufacturer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.manufacturer",
                        verbose_name="Производитель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Другой компонент",
                "verbose_name_plural": "Другие компоненты",
            },
        ),
        migrations.CreateModel(
            name="NetworkCard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "serial_number",
                    models.CharField(max_length=100, verbose_name="Серийный номер"),
                ),
                (
                    "inventory_number",
                    models.CharField(max_length=100, verbose_name="Инвентарный номер"),
                ),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Стоимость"
                    ),
                ),
                (
                    "start_date",
                    models.DateTimeField(verbose_name="Дата начала использования"),
                ),
                (
                    "end_date",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="Дата окончания использования",
                    ),
                ),
                ("speed", models.CharField(max_length=20, verbose_name="Скорость")),
                (
                    "card_type",
                    models.CharField(max_length=50, verbose_name="Тип сетевой карты"),
                ),
                (
                    "component_status",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.componentstatus",
                        verbose_name="Статус",
                    ),
                ),
                (
                    "in_computer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="equipments.computer",
                        verbose_name="Компьютер",
                    ),
                ),
                (
                    "manufacturer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.manufacturer",
                        verbose_name="Производитель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Сетевая карта",
                "verbose_name_plural": "Сетевые карты",
            },
        ),
        migrations.CreateModel(
            name="Motherboard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "serial_number",
                    models.CharField(max_length=100, verbose_name="Серийный номер"),
                ),
                (
                    "inventory_number",
                    models.CharField(max_length=100, verbose_name="Инвентарный номер"),
                ),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Стоимость"
                    ),
                ),
                (
                    "start_date",
                    models.DateTimeField(verbose_name="Дата начала использования"),
                ),
                (
                    "end_date",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="Дата окончания использования",
                    ),
                ),
                (
                    "component_status",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.componentstatus",
                        verbose_name="Статус",
                    ),
                ),
                (
                    "in_computer",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="equipments.computer",
                        verbose_name="Компьютер",
                    ),
                ),
                (
                    "manufacturer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.manufacturer",
                        verbose_name="Производитель",
                    ),
                ),
                (
                    "socket_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.sockettype",
                        verbose_name="Сокет",
                    ),
                ),
                (
                    "supported_memory_types",
                    models.ManyToManyField(
                        to="catalogs.memorytype",
                        verbose_name="Поддерживаемые типы памяти",
                    ),
                ),
            ],
            options={
                "verbose_name": "Материнская плата",
                "verbose_name_plural": "Материнские платы",
            },
        ),
        migrations.CreateModel(
            name="GraphicsCard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "serial_number",
                    models.CharField(max_length=100, verbose_name="Серийный номер"),
                ),
                (
                    "inventory_number",
                    models.CharField(max_length=100, verbose_name="Инвентарный номер"),
                ),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Стоимость"
                    ),
                ),
                (
                    "start_date",
                    models.DateTimeField(verbose_name="Дата начала использования"),
                ),
                (
                    "end_date",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="Дата окончания использования",
                    ),
                ),
                (
                    "memory",
                    models.CharField(max_length=20, verbose_name="Объем памяти"),
                ),
                ("frequency", models.IntegerField(verbose_name="Частота")),
                (
                    "component_status",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.componentstatus",
                        verbose_name="Статус",
                    ),
                ),
                (
                    "in_computer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="equipments.computer",
                        verbose_name="Компьютер",
                    ),
                ),
                (
                    "manufacturer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.manufacturer",
                        verbose_name="Производитель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Видеокарта",
                "verbose_name_plural": "Видеокарты",
            },
        ),
        migrations.CreateModel(
            name="Cooler",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "serial_number",
                    models.CharField(max_length=100, verbose_name="Серийный номер"),
                ),
                (
                    "inventory_number",
                    models.CharField(max_length=100, verbose_name="Инвентарный номер"),
                ),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Стоимость"
                    ),
                ),
                (
                    "start_date",
                    models.DateTimeField(verbose_name="Дата начала использования"),
                ),
                (
                    "end_date",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="Дата окончания использования",
                    ),
                ),
                (
                    "cooler_type",
                    models.CharField(max_length=50, verbose_name="Тип кулера"),
                ),
                ("size", models.CharField(max_length=20, verbose_name="Размер")),
                (
                    "component_status",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.componentstatus",
                        verbose_name="Статус",
                    ),
                ),
                (
                    "in_computer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="equipments.computer",
                        verbose_name="Компьютер",
                    ),
                ),
                (
                    "manufacturer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.manufacturer",
                        verbose_name="Производитель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Система охлаждения",
                "verbose_name_plural": "Системы охлаждения",
            },
        ),
        migrations.CreateModel(
            name="Case",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "serial_number",
                    models.CharField(max_length=100, verbose_name="Серийный номер"),
                ),
                (
                    "inventory_number",
                    models.CharField(max_length=100, verbose_name="Инвентарный номер"),
                ),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Стоимость"
                    ),
                ),
                (
                    "start_date",
                    models.DateTimeField(verbose_name="Дата начала использования"),
                ),
                (
                    "end_date",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="Дата окончания использования",
                    ),
                ),
                (
                    "case_type",
                    models.CharField(max_length=50, verbose_name="Тип корпуса"),
                ),
                ("num_bays", models.IntegerField(verbose_name="Количество отсеков")),
                (
                    "component_status",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.componentstatus",
                        verbose_name="Статус",
                    ),
                ),
                (
                    "in_computer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="equipments.computer",
                        verbose_name="Компьютер",
                    ),
                ),
                (
                    "manufacturer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogs.manufacturer",
                        verbose_name="Производитель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Корпус",
                "verbose_name_plural": "Корпуса",
            },
        ),
    ]
