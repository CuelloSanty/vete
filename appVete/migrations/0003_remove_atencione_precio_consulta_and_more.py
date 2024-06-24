# Generated by Django 5.0.4 on 2024-05-23 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appVete', '0002_rename_precio_insumos_atencione_precio_atencion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atencione',
            name='precio_consulta',
        ),
        migrations.AddField(
            model_name='atencione',
            name='precio_final',
            field=models.DecimalField(decimal_places=5, default=None, max_digits=6),
        ),
    ]
