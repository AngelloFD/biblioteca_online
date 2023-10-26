from django.db import models

# Create your models here.
class Categoria(models.Model):
   id_categoria = models.CharField(max_length=50, primary_key=True, unique=True, null=False, blank=False)
   nombre = models.CharField(max_length=50, null=False, blank=False)

   def __str__(self):
      return self.nombre

class Libro(models.Model):
   id_libro = models.CharField(max_length=100, primary_key=True, unique=True, null=False, blank=False)
   categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
   title = models.CharField(max_length=100, null=False, blank=False)
   author = models.CharField(max_length=50, null=False, blank=False)
   isbn = models.CharField(max_length=50, null=False, blank=False)
   summary = models.CharField(max_length=4000, null=False, blank=False)
   image = models.URLField(max_length=240, null=True, blank=False)

   def __str__(self):
      return self.title

class Estado(models.Model):
   id_estado = models.AutoField(primary_key=True, unique=True, null=False, blank=False)
   nombre = models.CharField(max_length=20, null=False, blank=False)

   def __str__(self):
      return self.id_estado + self.nombre

class Ejemplares(models.Model):
   id_ejemplar = models.CharField(max_length=100, primary_key=True, unique=True, null=False, blank=False)
   libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
   estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
   numero_ejemplar = models.IntegerField(null=False, blank=False)
   resumen = models.CharField(max_length=1000, null=False, blank=False)
   compuesto = models.CharField(max_length=20, null=False, blank=False) #TODO: pa q chcha era?

   def __str__(self):
      return self.id_ejemplar
   
class Prestamo(models.Model):
   id_prestamo = models.CharField(max_length=80, primary_key=True, unique=True, null=False, blank=False)
   id_ejemplar = models.ForeignKey(Ejemplares, on_delete=models.CASCADE)
   id_usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
   fecha_iniprestamo = models.DateField(null=True, blank=True)
   fecha_finprestamo = models.DateField(null=True, blank=True)
   fecha_devolucion = models.DateField(null=True, blank=True)

   def __str__(self):
      return self.id_prestamo + "_TO_" + self.id_usuario
   
class ReclamoUsuario(models.Model):
   id_reclamo = models.CharField(max_length=80, primary_key=True, unique=True, null=False, blank=False)
   id_prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
   descripcion = models.CharField(max_length=1000, null=False, blank=False)
   imagen = models.ImageField(upload_to='reclamos/', null=True, blank=False)
   fecha_creacion = models.DateField(auto_now_add=True, null=False, blank=False)

   def __str__(self):
      return self.id_reclamo + "_FROM_" + self.id_usuario

class Actividad(models.Model):
   id_actividad = models.CharField(max_length=50, primary_key=True, unique=True, null=False, blank=False)
   descripcion = models.CharField(max_length=500, null=False, blank=False)

   def __str__(self):
      return self.id_actividad
