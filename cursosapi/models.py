import random
from django.db.models.signals import pre_save, post_save
from django.db import models
from django.utils.text import slugify

estados =(
    ("ACTIVO", "Activo"),
    ("INACTIVO", "Inactivo"),
)
class Curso(models.Model):
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    relevancia = models.BooleanField()
    imagen = models.ImageField(upload_to='cursos', null = True, blank = True)
    slug = models.SlugField(unique= True, max_length=100, blank= True, null= True)
    estado = models.CharField(max_length=50, choices= estados, default= "ACTIVO")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.titulo} - {self.estado}"
    
    # Over Writting Save

    # def save(self, *args, **kwargs):
    #     # self.slug = slugify(self.titulo)
    #     super().save(*args, **kwargs)

# PRE SAVE
def curso_pre_save(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.titulo)

pre_save.connect(curso_pre_save, sender=Curso)

# POST SAVE 

# def curso_post_save(sender, instance, created, *args, **kwargs):
#     if created:
#         instance.slug = slugify(instance.titulo)
#         instance.save()

# post_save.connect(curso_post_save, sender=Curso)

class Profesor(models.Model):
    persona = models.CharField(max_length=150)
    documento = models.PositiveSmallIntegerField()
    fecha_nacimiento = models.DateField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self) -> str:
        return f"{self.persona} - {self.documento}"

class Alumno(models.Model):
    persona = models.CharField(max_length= 150)
    documento = models.PositiveSmallIntegerField()
    fecha_nacimiento = models.DateField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self) -> str:
        return f"{self.persona} - {self.documento}"

class Comision(models.Model):
    curso = models.ForeignKey(Curso, on_delete= models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete= models.PROTECT)
    cupos = models.PositiveSmallIntegerField()
    estado = models.CharField(max_length=50, choices = estados, default= "ACTIVO")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self) -> str:
        return f"{self.id} - {self.curso.titulo} - Cupos: {self.cupos}"

def comision_pre_save(instance, update_fields, *args, **kwargs):
    print(args, kwargs)
    if update_fields is None:
        while True:
            new_id = random.randint(100_000, 900_000)
            com = Comision.objects.filter(pk=new_id)
            if not com is None:
                break
        instance.id = new_id
pre_save.connect(comision_pre_save, sender=Comision)

# POST-SAVE

# def comision_post_save(instance, created, *args, **kwargs):
#     if created:
#         while True:
#             new_id = random.randint(100_000, 900_000)
#             com = Comision.objects.filter(pk=new_id)
#             if not com is None:
#                 break
#         instance.id = new_id
# post_save.connect(comision_pre_save, sender=Comision)

class ComisionDetail(models.Model):
    comision = models.ForeignKey(Comision, on_delete= models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    