from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from django.forms.widgets import Widget
from .models import Grupos, Horario, registro, HorarioDocente,Docente
from pedagogica.models import Semestre,Asignatura

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nombre', 'apellidoP', 'apellidoM',
                  'cedulaP','gradoEstudio', 'idDocenteUa']
        labels = {'nombre:Nombre del Docente',
                  'apellidoP: Apellido Paterno',
                  'apellidoM: Apellido Materno',
                  'cedulaP: Cedula Profesional',
                  'gradoEstudio: Grado de estudio',
                  'idDocenteUa: Unidad de Aprendizaje' }
                  

        
        widget = {'nombre': forms.TextInput,
                  'apellidoP': forms.TextInput,
                  'apellidoM': forms.TextInput,
                  'cedulaP': forms.TextInput,
                  'gradoEstudio': forms.TextInput,
                  'idDocenteUa': forms.MultipleChoiceField}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })
# Form para Horarios


class HorarioForm(forms.ModelForm):
    class Meta:
        model = HorarioDocente
        fields = ['horaInicio', 'horaSalida', 'fecha'
                  ]
        labels = {'horaInicio:Hora de inicio',
                  'horaSalida: Hora de salida',
                  'fecha: Fecha',
                  
                   }
                  

        
        widget = {'horaInicio': forms.TextInput,
                  'horaSalida': forms.TextInput,
                  'fecha': forms.TextInput,
                  }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

# Form para Grupo


class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupos
        fields = ['grupo'
                  ]
        labels = {'grupo:Nombre'
                   }
                  

        
        widget = {'Nombre': forms.TextInput,
                 }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })



# Form para registro


class registroForm(forms.ModelForm):
    class Meta:
        model = registro
        fields = ['nombre' , 'materia',
                  ]
        labels = {'nombre: Nombre',
                  'materia: Materia',
                   }
                  
        
        widget = {'nombre': forms.TextInput,
                  'materia': forms.TextInput,}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })


class salidaregistro(forms.ModelForm):
    class Meta:
        model = registro

        fields = ['horas']

        labels = {
                  'horas: Hora de Salida',
                 }

        widget = {'horas': forms.TextInput
                }
      
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })



# Form para cerar horario 

#no poner en los fields las relaciones 
class crearHorarioform(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['horaInicio', 'horaSalida', 'fecha',
                  ]
        labels = {'horaInicio:Hora de inicio',
                  'horaSalida: Hora de salida',
                  'fecha: Fecha',
                   }
                  

        
        widget = {'horaInicio': forms.TextInput,
                  'horaSalida': forms.TextInput,
                  'fecha': forms.TextInput,}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

class nuevoHorarioform(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['horaInicio', 'horaSalida', 'fecha',
                  ]
        labels = {'horaInicio:Hora de inicio',
                  'horaSalida: Hora de salida',
                  'fecha: Fecha',
                   }
                  

        
        widget = {'horaInicio': forms.TextInput,
                  'horaSalida': forms.TextInput,
                  'fecha': forms.TextInput,}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })


