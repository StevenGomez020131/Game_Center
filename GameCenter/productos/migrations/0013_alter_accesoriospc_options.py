# Generated by Django 5.0.6 on 2024-08-19 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0012_accesoriospc_delete_carrito'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accesoriospc',
            options={'ordering': ['-created'], 'verbose_name': 'Accesorio PC', 'verbose_name_plural': 'Accesorios PC'},
        ),
    ]
