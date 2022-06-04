from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from django.forms.widgets import Widget
from .models import Grupos, Horario, registro

# Form para Horarios


class HorarioForm(forms.ModelForm):
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

# Form para Grupo


class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupos
        fields = ['grupo','semestre','asignaturas'
                  ]
        labels = {'grupo:Nombre','semestre:Semestre','asignaturas:Asignatura'
                   }
                  

        
        widget = {'Nombre': forms.TextInput,
                'Semestre': forms.MultipleChoiceField,
                'Asignatura': forms.MultipleChoiceField
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