from django.db import models

# Create your models here.
class Materia(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    foto = models.ImageField(blank=True, null=True, upload_to="evidencia_img")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str__(self):
        return self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    materias_cursa = models.ManyToManyField(Materia, related_name='alumnos')
    foto = models.ImageField(blank=True, null=True, upload_to="evidencia_img")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Maestro(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    materias_imparte = models.ManyToManyField(Materia, related_name='maestro')
    foto = models.ImageField(blank=True, null=True, upload_to="evidencia_img")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

