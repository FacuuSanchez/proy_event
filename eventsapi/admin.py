from django.contrib import admin
from .models import Evento
# Register your models here.
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'descripcion_short', 'estado', 'relevancia', 'fecha_inicio',
    'fecha_fin', 'hora_inicio', 'hora_fin')
    list_filter = ('titulo',)
    search_fields = ('titulo',)

    def descripcion_short(self, obj):
        return f"{obj.descripcion[:40]}..."