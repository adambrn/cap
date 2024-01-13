# Generated by Django 4.2.4 on 2024-01-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("history", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="casehistory",
            name="end_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата возврата"
            ),
        ),
        migrations.AlterField(
            model_name="casehistory",
            name="start_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата выдачи"
            ),
        ),
        migrations.AlterField(
            model_name="coolerhistory",
            name="end_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата возврата"
            ),
        ),
        migrations.AlterField(
            model_name="coolerhistory",
            name="start_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата выдачи"
            ),
        ),
        migrations.AlterField(
            model_name="graphicscardhistory",
            name="end_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата возврата"
            ),
        ),
        migrations.AlterField(
            model_name="graphicscardhistory",
            name="start_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата выдачи"
            ),
        ),
        migrations.AlterField(
            model_name="motherboardhistory",
            name="end_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата возврата"
            ),
        ),
        migrations.AlterField(
            model_name="motherboardhistory",
            name="start_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата выдачи"
            ),
        ),
        migrations.AlterField(
            model_name="networkcardhistory",
            name="end_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата возврата"
            ),
        ),
        migrations.AlterField(
            model_name="networkcardhistory",
            name="start_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата выдачи"
            ),
        ),
        migrations.AlterField(
            model_name="othercomponenthistory",
            name="end_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата возврата"
            ),
        ),
        migrations.AlterField(
            model_name="othercomponenthistory",
            name="start_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата выдачи"
            ),
        ),
        migrations.AlterField(
            model_name="powersupplyhistory",
            name="end_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата возврата"
            ),
        ),
        migrations.AlterField(
            model_name="powersupplyhistory",
            name="start_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата выдачи"
            ),
        ),
        migrations.AlterField(
            model_name="processorhistory",
            name="end_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата возврата"
            ),
        ),
        migrations.AlterField(
            model_name="processorhistory",
            name="start_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата выдачи"
            ),
        ),
        migrations.AlterField(
            model_name="ramhistory",
            name="end_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата возврата"
            ),
        ),
        migrations.AlterField(
            model_name="ramhistory",
            name="start_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата выдачи"
            ),
        ),
        migrations.AlterField(
            model_name="storagehistory",
            name="end_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата возврата"
            ),
        ),
        migrations.AlterField(
            model_name="storagehistory",
            name="start_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата выдачи"
            ),
        ),
    ]