# Generated by Django 4.2.4 on 2024-01-13 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ComponentStatus",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Статус компонента",
                "verbose_name_plural": "Статусы компонентов",
            },
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "position",
                    models.CharField(max_length=100, verbose_name="Должность"),
                ),
            ],
            options={
                "verbose_name": "Сотрудник",
                "verbose_name_plural": "Сотрудники",
            },
        ),
        migrations.CreateModel(
            name="EquipmentCategory",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Категория оборудования",
                "verbose_name_plural": "Категории оборудования",
            },
        ),
        migrations.CreateModel(
            name="EquipmentStatus",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Статус оборудования",
                "verbose_name_plural": "Статусы оборудования",
            },
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("address", models.CharField(max_length=500, verbose_name="Адрес")),
            ],
            options={
                "verbose_name": "Местоположение",
                "verbose_name_plural": "Местоположения",
            },
        ),
        migrations.CreateModel(
            name="Manufacturer",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Производитель",
                "verbose_name_plural": "Производители",
            },
        ),
        migrations.CreateModel(
            name="MemoryType",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Тип памяти",
                "verbose_name_plural": "Типы памяти",
            },
        ),
        migrations.CreateModel(
            name="SocketType",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Тип сокета",
                "verbose_name_plural": "Типы сокетов",
            },
        ),
        migrations.CreateModel(
            name="StorageType",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Тип хранения",
                "verbose_name_plural": "Типы хранения",
            },
        ),
    ]
