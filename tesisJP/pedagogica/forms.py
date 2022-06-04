from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from django.forms.widgets import PasswordInput
from django.contrib.auth.models import User
from django.utils.regex_helper import Group
from .models import Plan_Estudio, Perfil_Egreso, Ambitos, Carrera, Ano, Semestre, Ejes, Asignatura, Competencias

# from para agregar usuarios

class PlanEstudioForm(forms.ModelForm):
    class Meta:
        model= Plan_Estudio

        fields = ['objetivo',]

        labels = {'objetivo: objetivo del plan de estudios' 
                  }

        widget = {'objetivo': forms.TextInput,

                  }

class Perfil_EgresoForm(forms.ModelForm):
    class Meta:
        model= Perfil_Egreso

        fields = ['descripcionPe',]

        labels = {'descripcionPe: descripcion plan de estudios' 
                  }

        widget = {'descripcionPe': forms.TextInput,
                    
                  } 
class AmbitosForm(forms.ModelForm):
    class Meta:
        model= Ambitos

        fields = ['descripcionAmb',]

        labels = {'descripcionAmb: descripcion del ambito' 
                  }

        widget = {'descripcionAmb': forms.TextInput,
                    
                  } 
class CarreraForm(forms.ModelForm):
    class Meta:
        model= Carrera

        fields = ['carrera', 'nom_corto',]

        labels = {'carrera: Carrera', 
                 'nom_corto: Nombre corto' 
                  }

        widget = {'carrera': forms.TextInput,
                 'nom_corto':  forms.TextInput,
                  } 
class AnoForm(forms.ModelForm):
    class Meta:
        model= Ano

        fields = ['ano',]

        labels = {'ano: año' 
                  }

        widget = {'ano': forms.TextInput,
                  } 
class SemestreForm(forms.ModelForm):
    class Meta:
        model= Ano

        fields = ['semestre',]

        labels = {'semestre: Semestre' 
                  }

        widget = {'semestre': forms.TextInput,
                  } 
class AsignaturaForm(forms.ModelForm):
    class Meta:
        model= Asignatura

        fields = ['asignatura', 'contenido', 'totalHsTeoricas', 'totalHsPracticas', 'total', 'creditos', ]

        labels = {'asignatura: Asignatura', 
                'contenido: Contenido', 
                'totalHsTeoricas: Total de Horas Teoricas', 
                'totalHsPracticas: Total de Horas Practicas', 
                'total: Total', 
                'creditos: Creditos'
                  }

        widget = {'asignatura': forms.TextInput,
                  'contenido': forms.TextInput,
                  'totalHsTeoricas' : forms.TextInput,
                  'totalHsPracticas' : forms.TextInput,
                  'total' : forms.TextInput,
                  'creditos' : forms.TextInput,
                  } 
class CompetenciasForm(forms.ModelForm):
    class Meta:
        model= Competencias

        fields = ['competencia', 'descripcionCompetencia',]

        labels = {'competencia: Competencia', 
                'descripcionCompetencia: Descripcion de la Competencia' 
                  }

        widget = {'competencia': forms.TextInput,
                 'descripcionCompetencia':  forms.TextInput,
                  } 