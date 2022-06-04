from django import forms
from django.contrib.auth import get_user
from django.forms import fields
from django.forms.models import ModelForm
from django.forms.widgets import PasswordInput, SelectMultiple
from django.core.validators import RegexValidator

from usuarios.models import User
from .models import User

# from para agregar usuarios

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(
        label="Introduce tu contraseña", widget=forms.PasswordInput)
    password_2 = forms.CharField(
        label="Confirma contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','estatura','peso', 'imagen', 'telefono','username',
                    'grado', 'curp','rfc', 'direccion', 'cedula','matricula','groups']
        exclude_fields = ['is_superuser', 'last_login',
                          'is_staff', 'is_active', 'date_joined', ]

        labels = {'first_name:Nombre del Usuario',
                    'last_name:Apellidos',
                    'estatura:Estatura' ,
                    'peso:Peso',
                    'imagen:Avatar',    
                    'telefono:Telefono',
                    'username:Usuario',
                    'grado:Grado',
                    'curp:Crup',
                    'rfc:Rfc',
                    'direccion:Dirección',
                    'cedula:Cedula',
                    'matricula:Matricula'}

        widget = {'nombre': forms.TextInput,
                  'aPaterno': forms.TextInput,
                  'aMaterno': forms.TextInput,
                  'estatura': forms.TextInput,
                  'peso': forms.TextInput,
                  'imagen': forms.TextInput,
                  'telefono': forms.TextInput,
                  'grado': forms.TextInput,
                  'curp': forms.TextInput,
                  'rfc': forms.TextInput,
                  'dirrecion': forms.TextInput,
                  'cedula': forms.TextInput,
                  'matricula': forms.TextInput,
                  'groups': SelectMultiple()
                  }

    def clean_email(self):
        '''
        Verify email is available.
        '''
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError(
                "El correo ingresado ya fue utilizado por otro usuario. Por favor, asigne uno diferente.")
        return email


    def clean_telefono(self):
        '''
        Verify phone is available.
        '''
        telefono = self.cleaned_data.get('telefono')
        if telefono:
            if not telefono.isdigit():
                raise forms.ValidationError(
                    "El nùmero telefònico sòlo debe contener dìgitos (10).")
            if not (len(telefono) == 10):
                raise forms.ValidationError(
                    "El nùmero telefònico debe tener 10 dìgitos.")
        return telefono

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error(
                "password_2", "El campo de confirmaciòn de contraseña no coincide.")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        # Se estan agregando los grupos al usuario
        for g in self.cleaned_data['groups']:
            user.groups.add(g)

        return user


class UsuarioEditForm(forms.ModelForm):

    password = forms.CharField(
        label="Introduce tu contraseña", widget=forms.PasswordInput)
    password_2 = forms.CharField(
        label="Confirma contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','estatura','peso', 'imagen', 'telefono','username',
                    'grado', 'curp','rfc', 'direccion', 'cedula','matricula','groups']
        exclude_fields = ['is_superuser', 'last_login',
                          'is_staff', 'is_active', 'date_joined', ]

        labels = {'first_name:Nombre del Usuario',
                    'last_name:Apellidos',
                    'estatura:Estatura' ,
                    'peso:Peso',
                    'imagen:Avatar',    
                    'telefono:Telefono',
                    'username:Usuario',
                    'grado:Grado',
                    'curp:Crup',
                    'rfc:Rfc',
                    'direccion:Dirección',
                    'cedula:Cedula',
                    'matricula:Matricula'}

        widget = {'nombre': forms.TextInput,
                  'aPaterno': forms.TextInput,
                  'aMaterno': forms.TextInput,
                  'estatura': forms.TextInput,
                  'peso': forms.TextInput,
                  'imagen': forms.TextInput,
                  'telefono': forms.TextInput,
                  'grado': forms.TextInput,
                  'curp': forms.TextInput,
                  'rfc': forms.TextInput,
                  'dirrecion': forms.TextInput,
                  'cedula': forms.TextInput,
                  'matricula': forms.TextInput,
                  'groups': SelectMultiple()
                  }

    # Validaciones para email y password
    '''def clean_email(self):
        
        #Verify email is available.
        
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs:
            raise forms.ValidationError(
                "El Email ingresado ya fue ocupado por otro Usuario")
        return email'''

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error(
                "password_2", "El Campo de Confirmacion de Contraseña NO Coincide")
        return cleaned_data

    '''def save(self, commit=True):
        form = super()

        
        # Save the provided password in hashed format
        user = form.save(commit=False)

        if user.password == self.cleaned_data["password"]:
            print("****NO hubo cambio de password")
        else:
            print("****Hubo cambio de password")
            user.set_password(self.cleaned_data["password"])

        user.save()
        # Se estan agregando los grupos al usuario
        user.groups.clear()

        print("Grupos: ", self.cleaned_data['groups'])
        for g in self.cleaned_data['groups']:
            user.groups.add(g)

        return user'''

