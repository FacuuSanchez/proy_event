from multiprocessing.managers import BaseManager
from django.db import models
from django.utils.text import slugify

estados =(
    ("ACTIVO", "Activo"),
    ("INACTIVO", "Inactivo"),
)


class Evento(models.Model):
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices= estados, default="ACTIVO")
    relevancia = models.BooleanField()
    imagen = models.ImageField(upload_to='eventos')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return f"{self.titulo} - {self.relevancia}"