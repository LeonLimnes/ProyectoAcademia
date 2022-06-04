from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from audioop import reverse
from django import views
from django.views.generic import View
from django.http import HttpResponseRedirect
from .mixins import ValidatePermissionRequiredMixin
from academica.forms import GrupoForm, HorarioForm, registroForm, salidaregistro
from academica.models import Grupos, Horario, registro
from pedagogica.models import Major
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
# Create your views here.
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template

from django.contrib.staticfiles import finders
from xhtml2pdf import pisa


#views.py
from django.shortcuts import render, redirect
 
from django.contrib.auth.models import *
from academica.filters import registrofiltro

import datetime

from django.db.models import Q 

# Create your views here.



class AcademicaView(LoginRequiredMixin, generic.ListView):
    model =  Grupos
    template_name= "indexA.html"
    context_object_name= "obj"
    login_url = "bases:login"


#...........................Crud Horario............................. 
#muestra Horario
class HorarioView(LoginRequiredMixin, ValidatePermissionRequiredMixin, generic.ListView):
    model = Horario
    template_name = "Horario/Horario_list.html"
    context_object_name = "obj"
    login_url = "bases:login"

#crear un nuevo horario
class HorarioNew(LoginRequiredMixin, ValidatePermissionRequiredMixin, generic.CreateView):
    model = Horario
    template_name = "Horario/Horario_form.html"
    context_object_name = "obj"
    form_class = HorarioForm
    succes_url = reverse_lazy("academica:Horario_list")
    login_url = "bases:login"
    

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

#actualizar horario
class HorarioEdit(LoginRequiredMixin, ValidatePermissionRequiredMixin, generic.UpdateView):
    model = Horario
    template_name = "Horario/Horario_form.html"
    context_object_name = "obj"
    form_class = HorarioForm
    success_url = reverse_lazy("academica:Horario_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

#eliminar horario
class HorarioDel(LoginRequiredMixin, ValidatePermissionRequiredMixin, generic.DeleteView):
   model = Horario
   template_name = 'Horario/Horario_del.html'
   context_objeject_name = 'obj'
   success_url = reverse_lazy('academica:Horario_list')


#...........................Crud Grupos.............................
#muestra grupo
class GrupoView(LoginRequiredMixin, ValidatePermissionRequiredMixin, generic.ListView):
    model = Grupos
    template_name = "grupo/grupo_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    


#crear un nuevo grupo
class GrupoNew(LoginRequiredMixin, ValidatePermissionRequiredMixin, generic.CreateView):
    model = Grupos
    template_name = "grupo/grupo_form.html"
    context_object_name = "obj"
    form_class = GrupoForm
    succes_url = reverse_lazy("academica:grupo_list")
    login_url = "bases:login"
    

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

#actualizar grupo
class GrupoEdit(LoginRequiredMixin, ValidatePermissionRequiredMixin, generic.UpdateView):
    model = Grupos
    template_name = "grupo/grupo_form.html"
    context_object_name = "obj"
    form_class = GrupoForm
    success_url = reverse_lazy("academica:grupo_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


#eliminar grupo
class GrupoDel(LoginRequiredMixin, ValidatePermissionRequiredMixin, generic.DeleteView):
   model = Grupos
   template_name = 'grupo/grupo_del.html'
   context_objeject_name = 'obj'
   success_url = reverse_lazy('academica:grupo_list')



#...........................Crud Registro.............................
#muestra registro
class registroView(LoginRequiredMixin, generic.ListView):
    model = registro
    template_name = "registro/registro_list.html"
    context_object_name = "obj"
    login_url = "bases:login"

def listar_usuario_cliente(request):
    busqueda = request.POST.get("buscar")
    usuario_cliente = registro.objects.all()

    if busqueda:
        usuario_cliente = registro.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(materia__icontains = busqueda) |
            Q(horae__icontains = busqueda)
        ).distinct()

    return render(request, 'registro/registro_list.html', {'usuario_cliente':usuario_cliente})
#buscar

def search(request):

     registro_list = registro.objects.all()
     registro_filter = registrofiltro(request.GET, queryset=registro_list)
     return render(request, 'registro_list.html', {'filter': registro_filter})


#crear un nuevo registro
class registroNew(LoginRequiredMixin, generic.CreateView):
    model = registro 
    template_name = "registro/registro_form.html"
    context_object_name = "obj"
    form_class = registroForm
    succes_url = reverse_lazy("academica:registro_list")
    login_url = "bases:login"
    

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
    def get(self, request, *args, **kwargs):
        docentetodo = Docente.objects.all() #se trae todos los datos de Horario
        UnidadAprendizajetodo = UnidadAprendizaje.objects.all()
        
        context = {
            'Docente': docentetodo, 
            'UnidadAprendizaje': UnidadAprendizajetodo
        }
        return render(request, 'registro/registro_form.html', context)

    def post(self, request, *args, **kwargs):
        form = registroForm(request.POST or None)
        print('***********************ya estoy en la vista********************************')
        print(form)
        if(request.POST and form.is_valid()):
            form.instance.uc = self.request.user
            rm=form.save()
           
            do = form.cleaned_data.get('nombre')
            print('***************',do)
            uniapre = form.cleaned_data.get('materia')
            print('***************',uniapre)
            #for item in do:
            rm.nombre.id #(item.id) 
            #for item in uniapre:
            rm.materia.id #(item.id)
            return HttpResponseRedirect(reverse_lazy('control_docente:registro_list'))   
        else:
            print('*********se genero un error*********')
            return render(request, 'registro/registro_form.html', {'form':form})

#actualizar registro
class salidadocente(LoginRequiredMixin, generic.UpdateView):
    model = registro
    template_name = "registro/docente_sale.html"
    context_object_name = "obj"
    form_class = salidaregistro
    success_url = reverse_lazy("academica:registro_list")
    login_url = "bases:login"
    myFilter = registrofiltro

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    

    def post(self, request, *args, **kwargs):
        pk =kwargs['pk']
        objsalida = registro.objects.get(id=pk) 
        print(objsalida)
        objsalida.horas = '{}'.format(datetime.datetime.now())
        objsalida.save()

        return HttpResponseRedirect(reverse_lazy("academica:registro_list"))
    
    

#para el pdf
class registroPdf(View):

    def get(self, request, *args, **kwargs):
        try:

            context = {
            'title': 'Reportes de Ingresos y salida del personal de docentes',
            'obj':registro.objects.all(),
            'emi':{'name':'Escuela Militar de Ingenieros', 'date':'Fecha:{}'.format(datetime.datetime.now().strftime("%A %d/%m/%Y")),
            'sd':'SISTEMA  DE CONTROL DE DOCENTE'}
            }
            template = get_template('registro/registro_PDF.html')   
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisa_status = pisa.CreatePDF( html, dest=response )
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy("academica:registro_list"))