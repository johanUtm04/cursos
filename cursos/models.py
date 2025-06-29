from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Curso")
    descripcion = models.TextField(verbose_name="Descripción")
    duracion = models.IntegerField(verbose_name="Duración en horas")
    precio = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio")
    disponible = models.BooleanField(default=True, verbose_name="Disponible")
    imagen = models.ImageField(upload_to='cursos/', null=True, blank=True, verbose_name="Imagen del Curso")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    def __str__(self):
        return self.nombre
    
class Meta:
    verbose_name = "Curso"               #nombre en singular
    verbose_name_plural = "Cursos"       #nombre en plural
    ordering = ['fecha_creacion']        #orden por fecha (más antigua primero)