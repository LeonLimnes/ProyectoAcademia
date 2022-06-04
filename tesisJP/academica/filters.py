#filters.py
from django.contrib.auth.models import *
from academica.models import registro
import django_filters
 
class registrofiltro(django_filters.FilterSet):
    class Meta:
        model = registro
        fields = ['nombre', 'materia', 'horae', ]
        
