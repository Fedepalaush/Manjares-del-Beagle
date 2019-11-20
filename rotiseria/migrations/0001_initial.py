
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
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
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Mapa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.CharField(max_length=50, null=True)),
                ('longitud', models.CharField(max_length=50, null=True)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('total', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('nombre_cliente', models.CharField(max_length=40)),
                ('descripcion', models.CharField(blank=True, max_length=200)),
                ('telefono_cliente', models.CharField(max_length=20)),
                ('pago', models.CharField(max_length=100)),
                ('bloque', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='rotiseria.Bloque')),
                ('estadoPedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rotiseria.EstadoPedido')),
                ('mapa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rotiseria.Mapa')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precioVariable', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('cantidad', models.PositiveIntegerField()),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rotiseria.Rol')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
