# Generated by Django 5.0.4 on 2024-05-23 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appVete', '0008_alter_articulo_peso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='talle',
            field=models.DecimalField(blank=True, decimal_places=1, default=None, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='vencimiento',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
