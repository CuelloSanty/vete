# Generated by Django 5.0.4 on 2024-05-23 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appVete', '0007_alter_articulo_peso_alter_articulo_talle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=5),
        ),
    ]
