# Generated by Django 2.2.3 on 2019-07-23 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_almacen', '0002_producto_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default='', max_length=200),
        ),
    ]
