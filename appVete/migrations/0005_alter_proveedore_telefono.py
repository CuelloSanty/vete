# Generated by Django 5.0.4 on 2024-05-23 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appVete', '0004_articulo_vencimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedore',
            name='telefono',
            field=models.CharField(max_length=15),
        ),
    ]