# Generated by Django 5.0.4 on 2024-04-19 14:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria_app', '0010_alter_clasificacionproducto_lista_clasificacion_producto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro_producto',
            name='clasificacion_Producto',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='libreria_app.clasificacionproducto', verbose_name='Tipo de producto'),
        ),
    ]
