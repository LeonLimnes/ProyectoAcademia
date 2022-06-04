from django import forms
from django.forms import CheckboxSelectMultiple, fields
from django.forms.models import ModelForm
from django.forms.widgets import PasswordInput, SelectMultiple
from django.contrib.auth.models import User
from django.utils.regex_helper import Group
from .models import Roadmap, Perfil_Egreso, Ambitos, Major, Semester, Axis, Subject, Competencias, Complementarias, Firmas, Ambitos_Ingreso, Certificacion_Est, Certificacion, Procedimiento_Acre, Procedimiento_Eval, Procedimientos, Recomendaciones_Met, Recomendaciones, Subrecomendaciones, Perfil_Ingreso, Catalogo_Ejes

# from para agregar usuarios



class PlanEstudioForm(forms.ModelForm):
    class Meta:
        model= Roadmap

        fields = ['objetive','name']

        labels = {'objetive: objetivo del plan de estudios' ,
                    'name: nombre',
                    
                  }

        widget = {'objetive': forms.TextInput,
                   'name': forms.TextInput
                  }
class Catalogo_EjesForm(forms.ModelForm):
    class Meta:
        model= Catalogo_Ejes

        fields = ['nombreejes']

        labels = {
                    'nombreejes: nombreejes',
                    
                  }

        widget = {
                   'nombreejes': forms.TextInput
                  }


class Perfil_EgresoForm(forms.ModelForm):
    class Meta:
        model= Perfil_Egreso

        fields = ['descripcionPe']

        labels = {'descripcionPe: descripcion  de estudios' 
                  }

        widget = {'descripcionPe': forms.TextInput
                    
                  } 
class AmbitosForm(forms.ModelForm):
    class Meta:
        model= Ambitos

        fields = ['descripcionAmb',]

        labels = {'descripcionAmb: descripcion del ambito' 
                  }

        widget = {'descripcionAmb': forms.TextInput
                    
                  } 
class CarreraForm(forms.ModelForm):
    class Meta:
        model= Major

        fields = ['name', 'abbreviation']

        labels = {'name: carrera',
                 'abbreviation: Nombre corto'
                  }

        widget = {'name': forms.TextInput,
                 'abbreviation':  forms.TextInput
                  } 
   
   
class AnoForm(forms.ModelForm):
    pass


class SemestreForm(forms.ModelForm):
    class Meta:
        model= Semester

        fields = ['period']

        labels = {'semester: Semestre'
                  }

        widget = {'semester': forms.TextInput
                  } 
class EjesForm(forms.ModelForm):
    class Meta:
        model= Axis

        fields = ['name', ]

        labels = {'name: Ejes'
                  }

        widget = {'name': forms.TextInput
                  } 
class AsignaturaForm(forms.ModelForm):
    class Meta:
        model= Subject

        fields = ['name', 'content', 'theory_hours', 'practice_hours', 'total_hours', 'credits']

        labels = {'asignatura: Asignatura', 
                'contenido: Contenido', 
                'totalHsTeoricas: Total de Horas Teoricas', 
                'totalHsPracticas: Total de Horas Practicas', 
                'total: Total', 
                'creditos: Creditos'
                  }

        widget = {'asignatura': forms.TextInput,
                  'contenido': forms.TextInput,
                  'totalHsTeoricas' : forms.FloatField,
                  'totalHsPracticas' : forms.FloatField,
                  'total' : forms.FloatField,
                  'creditos' : forms.FloatField
                  } 
class CompetenciasForm(forms.ModelForm):
    class Meta:
        model= Competencias

        fields = ['competencia', 'descripcionCompetencia']

        labels = {'competencia: Competencia', 
                'descripcionCompetencia: Descripcion de la Competencia' 
                  }

        widget = {'competencia': forms.TextInput,
                 'descripcionCompetencia':  forms.TextInput
                  } 
class ComplementariasForm(forms.ModelForm):
    class Meta:
        model= Complementarias

        fields = ['complementaria']

        labels = {'complementaria: Complementaria ' 
                  }

        widget = {'complementaria': forms.TextInput
                  } 
class FirmasForm(forms.ModelForm):
    class Meta:
        model= Firmas

        fields = ['grado', 'nombre_Completo','matricula']

        labels = {'grado: Grado', 
                'nombre_Completo: Nombre_Completo'
                'matricula: Matricula' 
                  }

        widget = {'grado': forms.TextInput,
                 'nombre_Completo':  forms.TextInput,
                 'matricula': forms.TextInput
                  } 
class Perfil_IngresoForm(forms.ModelForm):
    class Meta:
        model= Perfil_Ingreso

        fields = ['ambitos_MCCF']

        labels = {'ambitos_MCCF: Ambitos_MCCF'
                  }

        widget = {'Ambitos_MCCF': forms.TextInput
                  } 
class Ambitos_IngresoForm(forms.ModelForm):
    class Meta:
        model= Ambitos_Ingreso

        fields = ['descripcionAmbito',]

        labels = {'descripcionAmbito: Descripcion del ambito' 
                  }

        widget = {'descripcionAmbito': forms.TextInput
                    
                  } 
class Certificacion_EstForm(forms.ModelForm):
    class Meta:
        model= Certificacion_Est

        fields = ['certificacion_es']

        labels = {'certificacion_es: Certificacion_es' 
                  }

        widget = {'certificacion_es': forms.TextInput
                  } 
class CertificacionForm(forms.ModelForm):
    class Meta:
        model= Certificacion

        fields = ['descripcion_Cer']

        labels = {'descripcion_Cer: Descripcion_Cer' 
                  }

        widget = {'descripcion_Cer': forms.TextInput
                  } 
class Procedimiento_AcreForm(forms.ModelForm):
    class Meta:
        model= Procedimiento_Acre

        fields = ['acreditacion']

        labels = {'acreditacion: Acreditacion', 
                  }

        widget = {'acreditacion': forms.TextInput,
                  } 
class Procedimiento_EvalForm(forms.ModelForm):
    class Meta:
        model= Procedimiento_Eval

        fields = ['procedimientos_E']

        labels = {'procedimientos_E: Procedimientos_E', 
                  }

        widget = {'procedimientos_E': forms.TextInput,
                  } 
class ProcedimientosForm(forms.ModelForm):
    class Meta:
        model= Procedimientos

        fields = ['elemento', 'porcentaje',]

        labels = {'elemento: Elemento', 
                'porcentaje: Porcentaje' 
                  }

        widget = {'Elemento': forms.TextInput,
                 'porcentaje':  forms.TextInput,
                  } 
class Recomendaciones_MetForm(forms.ModelForm):
    class Meta:
        model= Recomendaciones_Met

        fields = ['recomendaciones']

        labels = {'recomendaciones: recomendaciones', 
                  }

        widget = {'recomendaciones': forms.TextInput,
                  } 
class RecomendacionesForm(forms.ModelForm):
    class Meta:
        model= Recomendaciones

        fields = ['subRecomendaciones']

        labels = {'subRecomendaciones: SubRecomendaciones' 
                  }

        widget = {'subRecomendaciones': forms.TextInput
                  } 
class SubrecomendacionesForm(forms.ModelForm):
    class Meta:
        model= Subrecomendaciones

        fields = ['subInciso']

        labels = {'subInciso: SubInciso', 
                  }
        widget = {'subInciso': forms.TextInput,
                  } 


        