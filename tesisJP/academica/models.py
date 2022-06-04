from django.db import models
from usuarios.models import User
from pedagogica.models import Asignatura,Semestre
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F
from bases.models import ClaseModelo
from django.urls import reverse
#Create your models here.

class HorarioDocente(ClaseModelo):
    horaInicio = models.TimeField(blank=False, null=False)
    horaSalida = models.TimeField(blank=False, null=False)
    fecha = models.CharField(blank=False, null=False, max_length=25)

    def get_absolute_url(self):
        return reverse('academica:Horario_list')

    def _str_(self):
        return self.fecha
    class Meta:
        verbose_name_plural='HorarioD'
    def save(self):
        super(HorarioDocente, self).save()

class Grupos(models.Model):
    grupo = models.CharField(max_length=50, blank=False, null=False)

    def get_absolute_url(self):
        return reverse('academica:grupo_list')


    def __str__(self): #lo que gresesara al consultar 
        return self.grupo

    class Meta:
        verbose_name_plural = 'Grupo'

    def save(self):
        super(Grupos,self).save()

class UnidadAprendizaje(ClaseModelo):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    
    idUaHorario = models.ManyToManyField('HorarioDocente', blank=True, related_name="UaHorario")
    idUaGrupo = models.ManyToManyField('Grupos', blank=True, related_name="UaGrupo")
    
    def _str_(self):
        return str(self.nombre)
    class Meta:
        verbose_name_plural='UnidadesAprendizaje'
    def save(self):
        super(UnidadAprendizaje, self).save()

class Docente(ClaseModelo):
    nombre = models.CharField(max_length=30, blank=False, null=False)
    apellidoP = models.CharField(max_length=25, blank=False, null=False)
    apellidoM = models.CharField(max_length=25, blank=False, null=False)
    gradoEstudio = models.CharField(max_length=15, blank=False, null=False)
    cedulaP = models.CharField(max_length=18, blank=False, null=False)

    idDocenteUa = models.ManyToManyField('UnidadAprendizaje', blank=True, related_name="docentes")

    def get_absolute_url(self):
        return reverse('academica:docente_list')

    def _str_(self):
        return str(self.nombre)
    
    def save(self):
        super(Docente, self).save()

    class Meta:
        verbose_name_plural='Docentes'



class registro(models.Model):
    
    horae = models.DateTimeField(auto_now_add=True)
    horas = models.DateTimeField(null=True)

    materia = models.ForeignKey(UnidadAprendizaje, on_delete=models.CASCADE)
    nombre = models.ForeignKey(Docente, on_delete=models.CASCADE)


    def _str_(self):
        return self.nombre
    class Meta:
        verbose_name_plural='registros'
    def save(self):
        super(registro, self).save()


class Horario(ClaseModelo):
    horaInicio = models.TimeField(blank=False, null=False)
    horaSalida = models.TimeField(blank=False, null=False)
    fecha = models.CharField(blank=False, null=False, max_length=25)
    dia=models.DateTimeField(blank=False, null=False)
    semestre= models.ForeignKey(Semestre, on_delete=models.CASCADE)
    grupo= models.ForeignKey(Grupos, on_delete=models.CASCADE)
    docente= models.ForeignKey(Docente, on_delete=models.CASCADE)
    asignaturas= models.ManyToManyField(
        Asignatura, blank=True, related_name="HorarioAsg"
    )

    def get_absolute_url(self):
        return reverse('academica:list_horario')

    def _str_(self):
        return self.fecha
    class Meta:
        verbose_name_plural='Horarios'
    def save(self):
        super(Horario, self).save()

