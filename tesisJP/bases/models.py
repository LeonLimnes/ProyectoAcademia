from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.conf import settings
# Create your models here.
class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    um = models.IntegerField(blank=True, null=True)

    uc = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)

    class Meta:
        abstract = True