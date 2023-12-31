# Generated by Django 4.2.5 on 2023-10-23 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id_actividad', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ejemplares',
            fields=[
                ('id_ejemplar', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('numero_ejemplar', models.IntegerField()),
                ('resumen', models.CharField(max_length=1000)),
                ('compuesto', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id_estado', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id_libro', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('isbn', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=4000)),
                ('image', models.URLField(max_length=240, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id_prestamo', models.CharField(max_length=80, primary_key=True, serialize=False, unique=True)),
                ('fecha_iniprestamo', models.DateField(blank=True, null=True)),
                ('fecha_finprestamo', models.DateField(blank=True, null=True)),
                ('fecha_devolucion', models.DateField(blank=True, null=True)),
                ('id_ejemplar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ejemplares')),
            ],
        ),
        migrations.CreateModel(
            name='ReclamoUsuario',
            fields=[
                ('id_reclamo', models.CharField(max_length=80, primary_key=True, serialize=False, unique=True)),
                ('descripcion', models.CharField(max_length=1000)),
                ('imagen', models.ImageField(null=True, upload_to='reclamos/')),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('id_prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.prestamo')),
            ],
        ),
    ]
