# Generated by Django 5.0.6 on 2024-08-19 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0008_remove_itemcarrito_carrito_delete_carrito_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='imagenesProductos',
        ),
        migrations.AlterField(
            model_name='accesoriosxbox',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
