# Generated by Django 4.2.4 on 2023-08-27 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("catalogs", "0003_delete_computermovementhistory"),
    ]

    operations = [
        migrations.CreateModel(
            name="PrintersHistory",
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
                (
                    "start_date",
                    models.DateField(blank=True, null=True, verbose_name="Дата выдачи"),
                ),
                (
                    "end_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата возврата"
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogs.employee",
                        verbose_name="Сотрудник",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogs.location",
                        verbose_name="Местоположение",
                    ),
                ),
                (
                    "printer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogs.printer",
                        verbose_name="Принтер",
                    ),
                ),
            ],
            options={
                "verbose_name": "История оборудования",
                "verbose_name_plural": "История оборудования",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ComputersHistory",
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
                (
                    "start_date",
                    models.DateField(blank=True, null=True, verbose_name="Дата выдачи"),
                ),
                (
                    "end_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата возврата"
                    ),
                ),
                (
                    "computer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogs.computer",
                        verbose_name="Компьютер",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogs.employee",
                        verbose_name="Сотрудник",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogs.location",
                        verbose_name="Местоположение",
                    ),
                ),
            ],
            options={
                "verbose_name": "История оборудования",
                "verbose_name_plural": "История оборудования",
                "abstract": False,
            },
        ),
    ]