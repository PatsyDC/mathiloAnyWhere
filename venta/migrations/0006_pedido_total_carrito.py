# Generated by Django 4.2.6 on 2023-11-03 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0005_departamento_remove_pedido_calle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='total_carrito',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
