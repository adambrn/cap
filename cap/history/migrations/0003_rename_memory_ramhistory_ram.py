# Generated by Django 4.2.4 on 2024-01-11 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_alter_casehistory_end_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ramhistory',
            old_name='memory',
            new_name='ram',
        ),
    ]