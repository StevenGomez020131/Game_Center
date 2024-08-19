# Generated by Django 5.0.6 on 2024-08-19 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0010_imagenesproductos_alter_accesoriosxbox_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto_id', models.PositiveIntegerField()),
                ('producto_tipo', models.CharField(choices=[('accesoriosXbox', 'Accesorios Xbox'), ('juegosXbox', 'Juegos Xbox'), ('accesoriosPlayStation', 'Accesorios PlayStation'), ('accesoriosNintendo', 'Accesorios Nintendo')], max_length=50)),
                ('cantidad', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]