from django.db import models
from usuarios.models import User
from pedagogica.models import Major,Semester
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F
from bases.models import ClaseModelo
from django.urls import reverse
#Create your models here.

class Horario(ClaseModelo):
    horaInicio = models.TimeField(blank=False, null=False)
    horaSalida = models.TimeField(blank=False, null=False)
    fecha = models.CharField(blank=False, null=False, max_length=25)

    asignaturas= models.ManyToManyField(
        Major, blank=True, related_name="HorarioAsg"
    )

    def get_absolute_url(self):
        return reverse('academica:Horario_list')

    def _str_(self):
        return self.fecha
    class Meta:
        verbose_name_plural='Horarios'
    def save(self):
        super(Horario, self).save()


class Grupos(models.Model):
    grupo = models.CharField(max_length=50, blank=False, null=False)

    semestre= models.ForeignKey(Semester, on_delete=models.CASCADE)

    asignaturas= models.ManyToManyField(
        Major, blank=True, related_name="GrupoAsg"
    )

    def get_absolute_url(self):
        return reverse('academica:grupo_list')


    def __str__(self): #lo que gresesara al consultar 
        return self.grupo

    class Meta:
        verbose_name_plural = 'Grupo'

    def save(self):
        super(Grupos,self).save()


class registro(models.Model):
    
    horae = models.DateTimeField(auto_now_add=True)
    horas = models.DateTimeField(null=True)
    materia = models.ForeignKey(Major, on_delete=models.CASCADE)
    nombre = models.ForeignKey(User, on_delete=models.CASCADE)


    def _str_(self):
        return self.nombre
    class Meta:
        verbose_name_plural='registros'
    def save(self):
        super(registro, self).save()