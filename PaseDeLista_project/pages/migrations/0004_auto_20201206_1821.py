# Generated by Django 3.1.4 on 2020-12-07 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20201206_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='fecha_asistencia',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='clase',
            name='fecha_clase',
            field=models.CharField(max_length=50),
        ),
    ]
