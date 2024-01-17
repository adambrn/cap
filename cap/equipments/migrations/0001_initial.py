# Generated by Django 4.2.4 on 2024-01-13 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("catalogs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Equipment",
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
                    "model",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Модель"
                    ),
                ),
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
                    "purchase_date",
                    models.DateTimeField(verbose_name="Дата приобретения"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogs.equipmentcategory",
                        verbose_name="Категория",
                    ),
                ),
                (
                    "equipment_status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogs.equipmentstatus",
                        verbose_name="Статус",
                    ),
                ),
                (
                    "manufacturer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogs.manufacturer",
                        verbose_name="Производитель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Оборудование",
                "verbose_name_plural": "Оборудование",
            },
        ),
        migrations.CreateModel(
            name="Computer",
            fields=[
                (
                    "equipment_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="equipments.equipment",
                    ),
                ),
            ],
            options={
                "verbose_name": "Компьютер",
                "verbose_name_plural": "Компьютеры",
            },
            bases=("equipments.equipment",),
        ),
        migrations.CreateModel(
            name="Monitor",
            fields=[
                (
                    "equipment_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="equipments.equipment",
                    ),
                ),
            ],
            options={
                "verbose_name": "Монитор",
                "verbose_name_plural": "Мониторы",
            },
            bases=("equipments.equipment",),
        ),
        migrations.CreateModel(
            name="NetworkDevice",
            fields=[
                (
                    "equipment_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="equipments.equipment",
                    ),
                ),
            ],
            options={
                "verbose_name": "Сетевое устройство",
                "verbose_name_plural": "Сетевые устройства",
            },
            bases=("equipments.equipment",),
        ),
        migrations.CreateModel(
            name="OtherEquipment",
            fields=[
                (
                    "equipment_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="equipments.equipment",
                    ),
                ),
            ],
            options={
                "verbose_name": "Другое оборудование",
                "verbose_name_plural": "Другое оборудование",
            },
            bases=("equipments.equipment",),
        ),
        migrations.CreateModel(
            name="Phone",
            fields=[
                (
                    "equipment_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="equipments.equipment",
                    ),
                ),
            ],
            options={
                "verbose_name": "Телефон",
                "verbose_name_plural": "Телефоны",
            },
            bases=("equipments.equipment",),
        ),
        migrations.CreateModel(
            name="Printer",
            fields=[
                (
                    "equipment_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="equipments.equipment",
                    ),
                ),
            ],
            options={
                "verbose_name": "Принтер",
                "verbose_name_plural": "Принтеры",
            },
            bases=("equipments.equipment",),
        ),
        migrations.CreateModel(
            name="Peripherals",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
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
                    "manufacturer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogs.manufacturer",
                        verbose_name="Производитель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Периферийное устройство",
                "verbose_name_plural": "Периферийные устройства",
            },
        ),
    ]
