from django.db import models

# Create your models here.
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


class Subrecomendaciones(models.Model):
    subInciso= models.CharField(max_length=400, blank=False, null=False)
    
    def __str__(self):
        return self.subInciso
    class Meta:
        verbose_name_plural = 'Subrecomendaciones'
    def save(self):
        super(Subrecomendaciones,self).save()

class Recomendaciones(models.Model):
    subRecomendaciones= models.CharField(max_length=400, blank=False, null=False)
    
    aSubRecomendaciones= models.ForeignKey(Subrecomendaciones, on_delete=models.CASCADE)

    def __str__(self):
        return self.subRecomendaciones
    class Meta:
        verbose_name_plural = 'Recomendaciones'
    def save(self):
        super(Recomendaciones,self).save()

class Recomendaciones_Met(models.Model):
    recomendaciones= models.CharField(max_length=400, blank=False, null=False)
    
    aProcedimientos= models.ForeignKey(Recomendaciones, on_delete=models.CASCADE)

    def __str__(self):
        return self.recomendaciones
    class Meta:
        verbose_name_plural = 'Recomendaciones_Met'
    def save(self):
        super(Recomendaciones_Met,self).save()

class Procedimientos(models.Model):
    elemento= models.CharField(max_length=400, blank=False, null=False)
    porcentaje= models.CharField(max_length=400, blank=False, null=False)

    def __str__(self):
        return self.elemento
    class Meta:
        verbose_name_plural = 'Procedimientos'
    def save(self):
        super(Procedimientos,self).save()

class Procedimiento_Eval(models.Model):
    procedimientos_E =models.CharField(max_length=400, blank=False, null=False)

    aProcedimientos= models.ForeignKey(Procedimientos, on_delete=models.CASCADE)

    def __str__(self):
        return self.procedimientos_E
    class Meta:
        verbose_name_plural = 'Procedimiento_Eval'
    def save(self):
        super(Procedimiento_Eval,self).save()


class Procedimiento_Acre(models.Model):
    acreditacion =models.CharField(max_length=400, blank=False, null=False)

    def __str__(self):
        return self.acreditacion
    class Meta:
        verbose_name_plural = 'Procedimiento_Acre'
    def save(self):
        super(Procedimiento_Acre,self).save()

class Certificacion(models.Model):
    descripcion_Cer =models.CharField(max_length=400, blank=False, null=False)


    def __str__(self):
        return self.descripcion_Cer
    class Meta:
        verbose_name_plural = 'Certificacion_Cer'
    def save(self):
        super(Certificacion,self).save()

class Certificacion_Est (models.Model):
    certificacion_es =models.CharField(max_length=400, blank=False, null=False)

    aCertificacion= models.ForeignKey(Certificacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.certificacion_es
    class Meta:
        verbose_name_plural = 'Certificacion_Est'
    def save(self):
        super(Certificacion_Est,self).save()


class Ambitos_Ingreso (models.Model):
    descripcionAmbito =models.CharField(max_length=400, blank=False, null=False)


    def __str__(self):
        return self.descripcionAmbito
    class Meta:
        verbose_name_plural = 'Ambitos_Ingreso'
    def save(self):
        super(Ambitos_Ingreso,self).save()


class Perfil_Ingreso (models.Model):
    ambitos_MCCF =models.CharField(max_length=400, blank=False, null=False)

    aAmbitosIngreso= models.ForeignKey(Ambitos_Ingreso, on_delete=models.CASCADE)

    def __str__(self):
        return self.ambitos_MCCF
    class Meta:
        verbose_name_plural = 'Perfil_Ingreso'
    def save(self):
        super(Perfil_Ingreso,self).save()


class Firmas(models.Model):
    grado =models.CharField(max_length=400, blank=False, null=False)
    nombre_Completo =models.CharField(max_length=400, blank=False, null=False)
    matricula =models.CharField(max_length=400, blank=False, null=False)

    def __str__(self):
        return self.grado
    class Meta:
        verbose_name_plural = 'Firmas'
    def save(self):
        super(Firmas,self).save()

class Complementarias (models.Model):
    complementaria =models.CharField(max_length=400, blank=False, null=False)

    def __str__(self):
        return self.complementaria
    class Meta:
        verbose_name_plural = 'Complementarias'
    def save(self):
        super(Complementarias,self).save()
    

class Competencias (models.Model):
    competencia =models.CharField(max_length=200, blank=False, null=False)
    descripcionCompetencia =models.CharField(max_length=400, blank=False, null=False)

    def __str__(self):
        return self.competencia
    class Meta:
        verbose_name_plural = 'Competencias'
    def save(self):
        super(Competencias,self).save()


class Ambitos(models.Model):
    descripcionAmb =models.CharField(max_length=200, blank=False, null=False)
    aCompetencia= models.ForeignKey(Competencias, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcionAmb
    class Meta:
        verbose_name_plural = 'Ambitos'
    def save(self):
        super(Ambitos,self).save()


class Perfil_Egreso(models.Model):
    descripcionPe =models.CharField(max_length=400, blank=False, null=False)

    ambito= models.ForeignKey(Ambitos, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcionPe 
    class Meta:
        verbose_name_plural = 'Perfil_Egresos'
    def save(self):
        super(Perfil_Egreso,self).save()


class Asignatura(models.Model):
    asignatura = models.CharField(max_length=100, blank=False, null=False)
    contenido =models.CharField(max_length=100, blank=False, null=False)
    totalHsTeoricas =models.FloatField(blank=False, null=False)
    totalHsPracticas =models.FloatField(blank=False, null=False)
    total =models.FloatField(blank=False, null=False)
    creditos =models.FloatField(blank=False, null=False)

    def __str__(self):
        return self.asignatura 
    class Meta:
        verbose_name_plural = 'Asignaturas'
    def save(self):
        super(Asignatura,self).save()


class Ejes(models.Model):
    ejes =models.CharField(max_length=100, blank=False, null=False)

    asignatura= models.ForeignKey(Asignatura, on_delete=models.CASCADE)

    def __str__(self):
        return self.ejes 
    class Meta:
        verbose_name_plural = 'Ejes'
    def save(self):
        super(Ejes,self).save()

class Semestre(models.Model):
    semestre =models.CharField(max_length=100, blank=False, null=False)

    ejes= models.ForeignKey(Ejes, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.semestre 
    class Meta:
        verbose_name_plural = 'Semestres'
    def save(self):
        super(Semestre,self).save()

class Ano(models.Model):
    ano = models.CharField(max_length=100, blank=False, null=False)

    semestre= models.ForeignKey(Semestre, on_delete=models.CASCADE)

    def __str__(self):
        return self.ano 
    class Meta:
        verbose_name_plural = 'Anos'
    def save(self):
        super(Ano,self).save()

class Carrera(models.Model):
    carrera = models.CharField(max_length=100, blank=False, null=False)
    nom_corto = models.CharField(max_length=100, blank=False, null=False)

    #Relacion hacia la tabla de año
    ano =models.ForeignKey(Ano, on_delete=models.CASCADE)
    

    def __str__(self): #lo que va a devolver de manera automatica
        return self.carrera 

    class Meta:
        verbose_name_plural = 'Carreras' #Consultar nombre plural
    
    def save(self):   #el metodo save va a guardar la informacion en estos campos
        super(Carrera,self).save()

        
class Plan_Estudio(models.Model):
    objetivo =models.CharField(max_length=400, blank=False, null=False)

    descripcionPEgre= models.ForeignKey(Perfil_Egreso, on_delete=models.CASCADE)    
    pCarrera= models.ForeignKey(Carrera, on_delete=models.CASCADE)
    pComplementarias= models.ForeignKey(Complementarias, on_delete=models.CASCADE)
    pFirmas= models.ForeignKey(Firmas, on_delete=models.CASCADE)
    pPerfil_Ingreso= models.ForeignKey(Perfil_Ingreso, on_delete=models.CASCADE)
    pProcedimiento_Acre= models.ForeignKey(Procedimiento_Acre, on_delete=models.CASCADE)
    pRecomendaciones_Met= models.ForeignKey(Recomendaciones_Met, on_delete=models.CASCADE)

    def __str__(self):
        return self.objetivo 
    class Meta:
        verbose_name_plural = 'Planes_Estudio'
    def save(self):
        super(Plan_Estudio,self).save()