from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Curso")
    descripcion = models.TextField(verbose_name="Descripción")
    duracion = models.IntegerField(verbose_name="Duración en horas")
    precio = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio en pesos (mxn)")
    disponible = models.BooleanField(default=True, verbose_name="Disponible")
    imagen = models.ImageField(upload_to='cursos/', null=True, blank=True, verbose_name="Imagen del Curso")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    def __str__(self):
        return self.nombre
# Actividad //////////////////////////////////////////////////////////
class Actividad(models.Model):
    clave = models.CharField(max_length=10)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    descripcion = RichTextField(verbose_name="actividad")
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
# Actividad //////////////////////////////////////////////////////////

class Meta:
    verbose_name = "Curso"               
    verbose_name_plural = "Cursos"       
    ordering = ['fecha_creacion']       

#Modelo del crud

#Definimos el modelo 'curso'
# class Curso(models.Model):
#     nombre = models.CharField(max_length=100)
#     duracion = models.IntegerField()  # o models.CharField si es tipo texto (ej: "3 meses")
#     precio = models.DecimalField(max_digits=10, decimal_places=2)
#     disponible = models.BooleanField(default=True)
#     fecha_creacion = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.nombre