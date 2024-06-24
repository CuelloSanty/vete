# Generated by Django 5.0.4 on 2024-05-23 20:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(blank=True, max_length=150)),
                ('img', models.URLField(blank=True, max_length=655, null=True)),
                ('marca', models.CharField(max_length=30)),
                ('tipo', models.CharField(choices=[('Med', 'Medicamento'), ('Alim', 'Alimento'), ('Acc', 'Accesorio')], default='Med', max_length=5)),
                ('unidad', models.CharField(choices=[('Bol', 'Bolsa'), ('Caj', 'Caja'), ('Sob', 'Sobre'), ('Com', 'Comprimido'), ('Uni', 'Unidad'), ('Kil', 'Kilos'), ('Gra', 'Gramos'), ('Mil', 'Mililitros'), ('Lit', 'Litros'), ('Otro', 'Otro')], default='Alim', max_length=5)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock_minimo', models.IntegerField(blank=True, null=True)),
                ('peso', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Atencione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField()),
                ('hora', models.TimeField()),
                ('tipo', models.CharField(choices=[('Med', 'Medica'), ('Pel', 'Peluqueria'), ('Amb', 'Ambos')], default='Med', max_length=5)),
                ('descripcion', models.CharField(max_length=150)),
                ('precio_insumos', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('FechaContratacion', models.DateField()),
                ('TurnoChoice', models.CharField(choices=[('Mañana', 'Mañana'), ('Tarde', 'Tarde'), ('Completa', 'Completa')], default='', max_length=8)),
                ('sueldo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('tipo', models.CharField(choices=[('Med', 'Medicamento'), ('Alim', 'Alimento'), ('Acc', 'Accesorio')], default='Med', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedore',
            fields=[
                ('cuit', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArticuloAtencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appVete.articulo')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appVete.atencione')),
            ],
        ),
        migrations.CreateModel(
            name='Adelanto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Monto', models.IntegerField()),
                ('FechaAdelanto', models.DateField()),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appVete.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('raza', models.CharField(blank=True, max_length=30, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appVete.cliente')),
            ],
        ),
        migrations.AddField(
            model_name='atencione',
            name='mascota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appVete.mascota'),
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appVete.articulo')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appVete.pedido')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appVete.proveedore'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appVete.proveedore'),
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appVete.cliente')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appVete.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.DecimalField(decimal_places=3, max_digits=3)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appVete.articulo')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appVete.venta')),
            ],
        ),
    ]
