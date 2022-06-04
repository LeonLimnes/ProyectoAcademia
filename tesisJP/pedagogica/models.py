from django.db import models

# Create your models here.
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


class Catalogo_Ejes(models.Model):
    nombreejes = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.nombreejes

    class Meta:
        verbose_name_plural = 'Nombreejes'

    def save(self, *args, **kwargs):
        super(Catalogo_Ejes, self).save()


class Subrecomendaciones(models.Model):
    subInciso = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.subInciso

    class Meta:
        verbose_name_plural = 'Subrecomendaciones'

    def save(self, *args, **kwargs):
        super(Subrecomendaciones, self).save()


class Recomendaciones(models.Model):
    subRecomendaciones = models.CharField(max_length=400, blank=True, null=True)

    aSubRecomendaciones = models.ForeignKey(Subrecomendaciones, on_delete=models.CASCADE)

    def __str__(self):
        return self.subRecomendaciones

    class Meta:
        verbose_name_plural = 'Recomendaciones'

    def save(self, *args, **kwargs):
        super(Recomendaciones, self).save()


class Recomendaciones_Met(models.Model):
    recomendaciones = models.CharField(max_length=400, blank=True, null=True)

    aProcedimientos = models.ForeignKey(Recomendaciones, on_delete=models.CASCADE)

    def __str__(self):
        return self.recomendaciones

    class Meta:
        verbose_name_plural = 'Recomendaciones_Met'

    def save(self, *args, **kwargs):
        super(Recomendaciones_Met, self).save()


class Procedimientos(models.Model):
    elemento = models.CharField(max_length=400, blank=True, null=True)
    porcentaje = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.elemento

    class Meta:
        verbose_name_plural = 'Procedimientos'

    def save(self, *args, **kwargs):
        super(Procedimientos, self).save()


class Procedimiento_Eval(models.Model):
    procedimientos_E = models.CharField(max_length=400, blank=True, null=True)

    aProcedimientos = models.ForeignKey(Procedimientos, on_delete=models.CASCADE)

    def __str__(self):
        return self.procedimientos_E

    class Meta:
        verbose_name_plural = 'Procedimiento_Eval'

    def save(self, *args, **kwargs):
        super(Procedimiento_Eval, self).save()


class Procedimiento_Acre(models.Model):
    acreditacion = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.acreditacion

    class Meta:
        verbose_name_plural = 'Procedimiento_Acre'

    def save(self, *args, **kwargs):
        super(Procedimiento_Acre, self).save()


class Certificacion(models.Model):
    descripcion_Cer = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.descripcion_Cer

    class Meta:
        verbose_name_plural = 'Certificacion_Cer'

    def save(self, *args, **kwargs):
        super(Certificacion, self).save()


class Certificacion_Est(models.Model):
    certificacion_es = models.CharField(max_length=400, blank=True, null=True)

    aCertificacion = models.ForeignKey(Certificacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.certificacion_es

    class Meta:
        verbose_name_plural = 'Certificacion_Est'

    def save(self, *args, **kwargs):
        super(Certificacion_Est, self).save()


class Ambitos_Ingreso(models.Model):
    descripcionAmbito = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.descripcionAmbito

    class Meta:
        verbose_name_plural = 'Ambitos_Ingreso'

    def save(self, *args, **kwargs):
        super(Ambitos_Ingreso, self).save()


class Perfil_Ingreso(models.Model):
    ambitos_MCCF = models.CharField(max_length=400, blank=True, null=True)

    aAmbitosIngreso = models.ForeignKey(Ambitos_Ingreso, on_delete=models.CASCADE)

    def __str__(self):
        return self.ambitos_MCCF

    class Meta:
        verbose_name_plural = 'Perfil_Ingreso'

    def save(self, *args, **kwargs):
        super(Perfil_Ingreso, self).save()


class Firmas(models.Model):
    grado = models.CharField(max_length=400, blank=True, null=True)
    nombre_Completo = models.CharField(max_length=400, blank=True, null=True)
    matricula = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.grado

    class Meta:
        verbose_name_plural = 'Firmas'

    def save(self, *args, **kwargs):
        super(Firmas, self).save()


class Complementarias(models.Model):
    complementaria = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.complementaria

    class Meta:
        verbose_name_plural = 'Complementarias'

    def save(self, *args, **kwargs):
        super(Complementarias, self).save()


class Competencias(models.Model):
    competencia = models.CharField(max_length=200, blank=True, null=True)
    descripcionCompetencia = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.competencia

    class Meta:
        verbose_name_plural = 'Competencias'

    def save(self, *args, **kwargs):
        super(Competencias, self).save()


class Ambitos(models.Model):
    descripcionAmb = models.CharField(max_length=200, blank=True, null=True)
    aCompetencia = models.ForeignKey(Competencias, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcionAmb

    class Meta:
        verbose_name_plural = 'Ambitos'

    def save(self, *args, **kwargs):
        super(Ambitos, self).save()


class Perfil_Egreso(models.Model):
    descripcionPe = models.CharField(max_length=400, blank=True, null=True)

    ambito = models.ForeignKey(Ambitos, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcionPe

    class Meta:
        verbose_name_plural = 'Perfil_Egresos'

    def save(self, *args, **kwargs):
        super(Perfil_Egreso, self).save()


class Axis(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=100, blank=False, null=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Eje'
        verbose_name_plural = 'Ejes'

    def save(self, *args, **kwargs):
        super(Axis, self).save()


class Semester(models.Model):
    period = models.IntegerField(blank=False, null=False)
    year = models.IntegerField(verbose_name='Año', blank=False, null=False)

    def __str__(self):
        return str(self.period)

    class Meta:
        verbose_name = 'Semestre'
        verbose_name_plural = 'Semestres'

    def save(self, *args, **kwargs):
        super(Semester, self).save()


class Subject(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=100, blank=False, null=False)
    content = models.CharField(verbose_name='Contenido', max_length=100, blank=False, null=False)
    theory_hours = models.FloatField(verbose_name='Horas teóricas', blank=False, null=False)
    practice_hours = models.FloatField(verbose_name='Horas prácticas', blank=False, null=False)
    total_hours = models.FloatField(verbose_name='Total de hors', blank=False, null=False)
    credits = models.FloatField(verbose_name='Créditos', blank=False, null=False)
    axis = models.ForeignKey(verbose_name='Eje', to=Axis, related_name='subjects', on_delete=models.CASCADE)
    semester = models.ForeignKey(verbose_name='Semestre', to=Semester, related_name='semester', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'

    def save(self, *args, **kwargs):
        self.total_hours = self.theory_hours + self.practice_hours
        super(Subject, self).save()


class Major(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=100, blank=False, null=False)
    abbreviation = models.CharField(verbose_name='Nombre corto', max_length=100, blank=False, null=False)
    subject = models.ManyToManyField(verbose_name='Asignaturas', to=Subject, related_name='subjects')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'

    def save(self, *args, **kwargs):
        super(Major, self).save()


class Roadmap(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=400, blank=False, null=False)
    objetive = models.CharField(verbose_name='Objetivo', max_length=400, blank=False, null=False)
    major = models.OneToOneField(verbose_name='Carrera', to=Major, related_name='major', on_delete=models.CASCADE)
    descripcionPEgre = models.ForeignKey(Perfil_Egreso, on_delete=models.CASCADE)
    pComplementarias = models.ForeignKey(Complementarias, on_delete=models.CASCADE)
    pFirmas = models.ForeignKey(Firmas, on_delete=models.CASCADE)
    pPerfil_Ingreso = models.ForeignKey(Perfil_Ingreso, on_delete=models.CASCADE)
    pProcedimiento_Acre = models.ForeignKey(Procedimiento_Acre, on_delete=models.CASCADE)
    pRecomendaciones_Met = models.ForeignKey(Recomendaciones_Met, on_delete=models.CASCADE)
    pCertificacion_Est = models.ForeignKey(Certificacion_Est, on_delete=models.CASCADE)
    pProcedimiento_Eval = models.ForeignKey(Procedimiento_Eval, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Plan de Estudio'
        verbose_name_plural = 'Planes de Estudio'

    def save(self, *args, **kwargs):
        super(Roadmap, self).save()
