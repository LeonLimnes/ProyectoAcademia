from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django.contrib.auth import models


from django.contrib.auth.models import User
from .models import User
from django.shortcuts import get_object_or_404
from usuarios.models import User  # modelo user personaliozado
from .forms import UsuarioForm, UsuarioEditForm
from django.urls import reverse_lazy, reverse
from .mixins import ValidatePermissionRequiredMixin
from django.contrib.auth.hashers import check_password

# Bibliotecas para la impresion del PDF
#import os
#from django.conf import settings
#from django.http import HttpResponse, JsonResponse
#from django.template import Context
#from django.template.loader import get_template
#from xhtml2pdf import pisa
#from django.conf.global_settings import MEDIA_URL, STATIC_URL
# Create your views here.



class UsuarioView(LoginRequiredMixin, generic.ListView):
    model =  User#modelo a utilizar 
    template_name= "u_list.html"#nombre del template a utilizar 
    context_object_name= "obj"#es un objeto deonde podemos guardar info que vamos hacer llegar al template
    login_url = "bases:login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Usuarios'
        context['create_url'] = ''
        context['list_url'] = reverse_lazy('user:usuarios_list')
        context['entity'] = 'Usuarios'
        return context

class CrearUsuario(LoginRequiredMixin,ValidatePermissionRequiredMixin, generic.CreateView):
    model =  User#modelo a utilizar 
    permission_required = 'add_usuarios'
    template_name= "formU.html"#nombre del template a utilizar 
    context_object_name= "obj"#es un objeto deonde podemos guardar info que vamos hacer llegar al template
    form_class = UsuarioForm
    succes_url = reverse_lazy("usuarios:usuarios_list")
    login_url = "bases:login"
    
    def get(self, request, *args, **kwargs):
        grupos = models.Group.objects.all()
        context = {
            'grupos': grupos
        }
        return render(request, 'formU.html', context)

    def form_valid(self, form):
        form.instance.uc = self.request.user

        # email = form.cleaned_data.get('email')
        # username = form.cleaned_data.get('username')

        print("******image: ", form.cleaned_data.get('image'))

        # En el Form ya se hace la validacion del campo de Email y Password
        '''
        # Se valida que el email no este siendo utilizado por alguien mas
        coincidencias = User.objects.filter(email=email).count()
        if (coincidencias > 0):
            form.add_error(
                'email', "El Email Ingresado ya Fue Ocupado Por Otro Usuario, Por favor, Introduzca uno Diferente")
            return super().form_invalid(form)

        # Se valida que el nombre de usuario no este siendo utilizado por alguien mas
        coincidencias = User.objects.filter(username=username).count()
        if (coincidencias > 0):
            form.add_error(
                'username', "El Nombre de Usuario Ingresado ya Fue Ocupado por Otro Usuario, Por favor, Introduzca uno Diferente")
            return super().form_invalid(form)'''

        # Se registra el nuevo usuario
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form, **kwargs):
        #grupos = models.Group.objects.all()
        context = self.get_context_data(**kwargs)
        context['form'] = form
        #context['grupos'] = grupos
        return self.render_to_response(context)

class ActualizarUsuario(LoginRequiredMixin, generic.UpdateView):
    model = User
    template_name = "formU.html"
    context_object_name = "obj"
    form_class = UsuarioEditForm
    success_url = reverse_lazy("usuarios:usuarios_list")
    login_url = "bases:login"

    def get(self, request, *args, **kwargs):
        # se indica en el formulario que se va a hacer un edit
        # Se obtiene ID del Doctor
        pk = self.kwargs['pk']

        form = User.objects.get(id=pk)
        # print("Grupos Edit: ", form.groups.all())
        # Obtiene los grupos existentes que no estan asignados al usuario
        gruposNoSeleccionados = models.Group.objects.all().exclude(id__in=form.groups.all())
        # print("***GruposNoSeleccionados: ", gruposNoSeleccionados)
        # print("***GruposSeleccionados: ", form.groups.all())

        context = {'form': form, 'edit': True, 'GNS': gruposNoSeleccionados}
        return render(request, 'formU.html', context)

    def form_valid(self, form, **kwargs):
        cambio = False
        # Se agrega al formulario el campo um para indicar el usuario que modifico el registro
        form.instance.um = self.request.user.id

        # Se valida que si hace un cambio de email, no agregue uno existente en la BD
        # Se obtiene ID del Doctor
        pk = self.kwargs['pk']

        emailRecibido = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        userFormulario = User.objects.get(pk=pk)

        # field_value = getattr(userFormulario, 'email')
        # print(userFormulario)
        if emailRecibido != userFormulario.email:
            if User.objects.filter(email=emailRecibido):
                form.add_error(
                    'email', "El Email ingresado ya fue ocupado por otro Usuario. Por favor, Introduzca uno Diferente")
                return super().form_invalid(form)

        # Valida si hubo un cambio de password, para validar si un password en texto plano es igual a uno hasheado en a BD
        # se usa la funcion check_password(password, encoded)
        if not password == userFormulario.password:
            #print("----Hubo Cambio de password")
            cambio = True
            # form.set_password(password)

        user = form.save()
        if cambio:
            #print("----Hubo Cambio de password")
            user.set_password(password)
        # Se estan agregando los grupos al usuario
        user.groups.clear()

        #print("Grupos: ", form.cleaned_data['groups'])
        for g in form.cleaned_data['groups']:
            user.groups.add(g)

        return super().form_valid(form)

class BorrarUsuario(LoginRequiredMixin, generic.DeleteView):
    model = User
    template_name = 'eliminarU.html'
    context_objeject_name = 'obj'
    success_url = reverse_lazy('usuarios:usuarios_list')






