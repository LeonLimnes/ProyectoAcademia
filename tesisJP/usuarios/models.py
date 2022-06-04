from django.db import models
from bases.models import ClaseModelo
from django.contrib.auth.models import AbstractUser
from django.conf.global_settings import MEDIA_URL, STATIC_URL
from django.urls import reverse
from pedagogica.models import Subject
from crum import get_current_request

# Create your models here.
class User(AbstractUser):

    estatura = models.FloatField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    imagen = models.ImageField(
        upload_to='img/user/',blank=True, null=True
    )
    telefono= models.CharField(max_length=10, blank=True, null=True)
    grado = models.CharField(max_length=30, blank=True, null=True) 
    curp = models.CharField(max_length=18, blank=True, null=True)
    rfc = models.CharField(max_length=13, blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    cedula =models.CharField(max_length=50, blank=True, null=True)
    matricula=models.CharField(max_length=10, blank=True, null=True)


    asignaturas= models.ManyToManyField(
        Subject, blank=True, related_name="UserAsg"
    )

    def get_absolute_url(self):
        return reverse('usuarios:usuarios_list')

    def _str_(self):
        return str(self.first_name)

    def get_image(slef):
        if self.imagen:
            return '{}{}'. format (MEDIA_URL, self.image)
        return '{}{}'. format(STATIC_URL,'img/empty.png' )

    def get_group_session(self):
        try:
            request = get_current_request()
            groups = self.groups.all()
            if groups.exists():
                if 'group' not in request.session:
                    request.session['group'] = groups[0]
        except:
            pass

    class Meta:
        verbose_name_plural='Docentes'



