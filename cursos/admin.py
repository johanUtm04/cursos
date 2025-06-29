from django.contrib import admin
from .models import Curso

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'duracion', 'precio', 'disponible', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    date_hierarchy = 'fecha_creacion'
    list_filter = ('disponible', 'duracion')
    ordering = ['fecha_creacion']

# 👉 Aquí registras el modelo con su configuración admin personalizada:
admin.site.register(Curso, CursoAdmin)
