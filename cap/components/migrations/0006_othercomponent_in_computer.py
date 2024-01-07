# Generated by Django 4.2.4 on 2024-01-07 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("equipments", "0003_alter_equipment_purchase_date"),
        ("components", "0005_alter_case_start_date_alter_cooler_start_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="othercomponent",
            name="in_computer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="equipments.computer",
                verbose_name="Компьютер",
            ),
        ),
    ]
