# Generated by Django 5.0.4 on 2024-05-23 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appVete', '0009_alter_articulo_peso_alter_articulo_talle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='descripcion',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]