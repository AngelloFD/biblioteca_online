# Generated by Django 4.2.5 on 2023-10-31 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_ejemplares_estado_remove_ejemplares_libro_and_more'),
        ('prestamos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamousuario',
            name='id_prestamo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestamos.prestamo'),
        ),
        migrations.DeleteModel(
            name='Ejemplares',
        ),
        migrations.DeleteModel(
            name='Prestamo',
        ),
    ]
