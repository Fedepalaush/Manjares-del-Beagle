# Generated by Django 2.1.1 on 2019-10-22 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoría',
            fields=[
                ('nombre', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('dni', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estadopedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mapa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.CharField(max_length=50, null=True)),
                ('longitud', models.CharField(max_length=50, null=True)),
                ('direccion', models.CharField(max_length=50)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rotiseria.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('total', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('bloque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rotiseria.Bloque')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rotiseria.Cliente')),
                ('estadoPedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rotiseria.Estadopedido')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precioVariable', models.IntegerField()),
                ('subtotal', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rotiseria.Pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=50)),
                ('foto', models.ImageField(null=True, upload_to='rotiseria/images/')),
                ('precioActual', models.DecimalField(decimal_places=3, max_digits=8)),
                ('ganancia', models.IntegerField(null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rotiseria.Categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('alias', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('contrasenia', models.CharField(max_length=12)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rotiseria.Rol')),
            ],
        ),
        migrations.AddField(
            model_name='pedidoproducto',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rotiseria.Producto'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='productos',
            field=models.ManyToManyField(to='rotiseria.Producto'),
        ),
        migrations.AddField(
            model_name='bloque',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rotiseria.Usuario'),
        ),
    ]
