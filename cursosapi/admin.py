from django.contrib import admin
from .models import Comision, Curso, Profesor, Alumno, ComisionDetail

# Register your models here.
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'descripcion_short', 'relevancia', 'slug', 'estado')
    list_filter = ('titulo',)
    search_fields = ('titulo',)

    def descripcion_short(self, obj):
        return f"{obj.descripcion[:40]}..."

@admin.register(Comision)
class ComisionAdmin(admin.ModelAdmin):
    list_display = ('curso', 'cupos', 'estado', 'fecha_inicio', 'fecha_fin', 'hora_inicio', 'hora_fin')
    list_filter = ('curso__titulo',)
    search_fields = ('curso__titulo',)

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('persona', 'documento', 'fecha_nacimiento')
    list_filter = ('persona', 'documento')
    search_fields = ('persona', 'documento')

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('persona', 'documento', 'fecha_nacimiento')
    list_filter = ('persona', 'documento')
    search_fields = ('persona', 'documento')

@admin.register(ComisionDetail)
class ComisionDetailAdmin(admin.ModelAdmin):
    list_display = ('comision', 'alumno')
    list_filter = ('comision', 'alumno__persona')
    search_fields = ('comision', 'alumno__persona')
