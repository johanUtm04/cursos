from django.contrib import admin
from .models import Curso
from .models import Actividad


class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'duracion', 'precio', 'disponible', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    date_hierarchy = 'fecha_creacion'
    list_filter = ('disponible', 'duracion')
    ordering = ['fecha_creacion']

class ActividadAdmin(admin.ModelAdmin):
    list_display = ('clave', 'curso', 'descripcion_corta', 'fecha_creacion')
    search_fields = ('clave', 'descripcion')
    list_filter = ('fecha_creacion', 'curso')
    ordering = ['fecha_creacion']

    def descripcion_corta(self, obj):
        return (obj.descripcion[:50] + '...') if len(obj.descripcion) > 50 else obj.descripcion

    descripcion_corta.short_description = 'Descripción'



admin.site.register(Curso, CursoAdmin)

admin.site.register(Actividad, ActividadAdmin)