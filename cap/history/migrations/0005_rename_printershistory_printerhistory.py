# Generated by Django 4.2.4 on 2023-09-17 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalogs", "0001_initial"),
        ("equipments", "0002_monitor"),
        ("history", "0004_alter_computerhistory_employee_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="PrintersHistory",
            new_name="PrinterHistory",
        ),
    ]
