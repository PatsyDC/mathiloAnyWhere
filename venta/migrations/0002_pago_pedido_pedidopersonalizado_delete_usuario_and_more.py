# Generated by Django 4.2.6 on 2023-10-30 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma', models.CharField(max_length=250)),
                ('descripcion', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'pagos',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True)),
                ('fecha_de_entrega', models.DateTimeField()),
                ('calle', models.CharField(max_length=250)),
                ('stock', models.IntegerField(default=0)),
                ('distrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.distrito')),
            ],
            options={
                'verbose_name_plural': 'pedidos',
            },
        ),
        migrations.CreateModel(
            name='PedidoPersonalizado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(max_length=540)),
                ('número_celular', models.IntegerField()),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos_id_user', to=settings.AUTH_USER_MODEL)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos_username', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'pedidos_personalizados',
            },
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pedido',
            name='id_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.producto'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_pedido', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pedido',
            name='pago',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.pago'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.provincia'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='username_pedido', to=settings.AUTH_USER_MODEL),
        ),
    ]
