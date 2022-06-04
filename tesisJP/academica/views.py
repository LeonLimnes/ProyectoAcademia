from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from audioop import reverse
from django import views
from django.views.generic import View
from django.http import HttpResponseRedirect
from .mixins import ValidatePermissionRequiredMixin
from academica.forms import GrupoForm, HorarioForm, registroForm, salidaregistro, crearHorarioform,nuevoHorarioform, DocenteForm
from academica.models import Grupos, Horario, registro, Docente,HorarioDocente,UnidadAprendizaje
from pedagogica.models import Asignatura,Semestre
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


class DocenteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, generic.ListView):
    model = Docente
    permission_required = 'view_docente'    
    template_name = "control_docente/docente/docente_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
    #def get(self, request, *args, **kwargs):


#crear un nuevo usuario 
class DocenteNew(LoginRequiredMixin, ValidatePermissionRequiredMixin, generic.CreateView):
    model = Docente 
    template_name = "control_docente/docente/docente_form.html"                 
    context_object_name = "obj"
    form_class = DocenteForm
    succes_url = reverse_lazy("academica:docente_list")
    login_url = "bases:login"
    #def form_valid(self, form):
        #form.instance.uc = self.request.user
        #return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        UAtodo = UnidadAprendizaje.objects.all() #se trae todos los datos de unidad de aprendizaje
      
        
        context = {
            'UA': UAtodo, 

        }
        return render(request, 'control_docente/docente/docente_form.html', context)

    def post(self, request, *args, **kwargs):
        form = DocenteForm(request.POST or None)

        if(request.POST and form.is_valid()):
            form.instance.uc = self.request.user
            docente=form.save()
            uni = form.cleaned_data.get('idDocenteUa')
            for item in uni:
                docente.idDocenteUa.add(item.id)
            return HttpResponseRedirect(reverse_lazy('academica:docente_list'))   
        else:
            return render(request, 'control_docente/docente/docente_list.html', {'form':form})


#actualizar docente
class DocenteEdit(LoginRequiredMixin, ValidatePermissionRequiredMixin, generic.UpdateView):
    model = Docente
    template_name = "control_docente/docente/docente_form.html"
    context_object_name = "obj"
    form_class = DocenteForm
    success_url = reverse_lazy("academica:docente_list")
    login_url = "bases:login"

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        doc = Docente.objects.filter(id=pk)  
        #rt = doc.idDocenteUa.all() #obtener todas las unidades de aprendizaje del docente     
        doc=doc[0]#quita el encapsulamiento del queryset
        
        obj = {
            'obj': doc, 

        }
        return render(request, 'control_docente/docente/docente_form.html', obj)
    
    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        docente = Docente.objects.get(pk=pk)
        form = DocenteForm(request.POST or None , instance=docente)

        if(request.POST and form.is_valid()):
            form.instance.uc = self.request.user
            docente=form.save()
            uni = form.cleaned_data.get('idDocenteUa')
            for item in uni:
                docente.idDocenteUa.add(item.id)
            return HttpResponseRedirect(reverse_lazy('academica:docente_list'))   
        else:
            return render(request, 'control_docente/docente/docente_list.html', {'form':form})

    
#eliminar docente
class DocenteDel(LoginRequiredMixin, ValidatePermissionRequiredMixin, generic.DeleteView):
   model = Docente
   template_name = 'control_docente/docente/docente_del.html'
   context_objeject_name = 'obj'
   success_url = reverse_lazy('academica:docente_list')



#...........................Crud Horario............................. 
#muestra Horario
class HorarioView(LoginRequiredMixin, ValidatePermissionRequiredMixin, generic.ListView):
    model = HorarioDocente
    template_name = "control_docente/Horario/Horario_list.html"
    context_object_name = "obj"
    login_url = "bases:login"

#crear un nuevo horario
class HorarioNew(LoginRequiredMixin, ValidatePermissionRequiredMixin, generic.CreateView):
    model = HorarioDocente
    template_name = "control_docente/Horario/Horario_form.html"
    context_object_name = "obj"
    form_class = HorarioForm
    succes_url = reverse_lazy("academica:Horario_list")
    login_url = "bases:login"
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

    
#actualizar horario
class HorarioEdit(LoginRequiredMixin, ValidatePermissionRequiredMixin, generic.UpdateView):
    model = HorarioDocente
    template_name = "control_docente/Horario/Horario_form.html"
    context_object_name = "obj"
    form_class = HorarioForm
    success_url = reverse_lazy("academica:Horario_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

#eliminar horario
class HorarioDel(LoginRequiredMixin, ValidatePermissionRequiredMixin, generic.DeleteView):
   model = HorarioDocente
   template_name = 'control_docente/Horario/Horario_del.html'
   context_objeject_name = 'obj'
   success_url = reverse_lazy('academica:Horario_list')


#...........................Crud Grupos.............................
#muestra grupo
class GrupoView(LoginRequiredMixin, ValidatePermissionRequiredMixin, generic.ListView):
    model = Grupos
    template_name = "control_docente/grupo/grupo_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    


#crear un nuevo grupo
class GrupoNew(LoginRequiredMixin, ValidatePermissionRequiredMixin, generic.CreateView):
    model = Grupos
    template_name = "control_docente/grupo/grupo_form.html"
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
    template_name = "control_docente/grupo/grupo_form.html"
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
   template_name = 'control_docente/grupo/grupo_del.html'
   context_objeject_name = 'obj'
   success_url = reverse_lazy('academica:grupo_list')



#...........................Crud Registro.............................
#muestra registro
class registroView(LoginRequiredMixin, generic.ListView):
    model = registro
    template_name = "control_docente/registro/registro_list.html"
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

    return render(request, 'control_docente/registro/registro_list.html', {'usuario_cliente':usuario_cliente})
#buscar

def search(request):

     registro_list = registro.objects.all()
     registro_filter = registrofiltro(request.GET, queryset=registro_list)
     return render(request, 'registro_list.html', {'filter': registro_filter})


#crear un nuevo registro
class registroNew(LoginRequiredMixin, generic.CreateView):
    model = registro 
    template_name = "control_docente/registro/registro_form.html"
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
        return render(request, 'control_docente/registro/registro_form.html', context)

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
            return HttpResponseRedirect(reverse_lazy('academica:registro_list'))   
        else:
            print('*********se genero un error*********')
            return render(request, 'control_docente/registro/registro_form.html', {'form':form})

#actualizar registro
class salidadocente(LoginRequiredMixin, generic.UpdateView):
    model = registro
    template_name = "control_docente/registro/docente_sale.html"
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
            template = get_template('control_docente/registro/registro_PDF.html')   
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisa_status = pisa.CreatePDF( html, dest=response )
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy("academica:registro_list"))



class CrearHorarioView(generic.TemplateView):
    model = Horario
    template_name='Horarios/horario_crear.html'
    context_object_name = "obj"
    form_class = crearHorarioform
    success_url = reverse_lazy("academica:crear_horario")
    login_url = "bases:login"
   
      
    """def get(self, request, *args, **kwargs):
        pass
        return HttpResponseRedirect(reverse_lazy("academica:crear_horario"))"""

    def form_valid(self, form):
        pass
        return HttpResponseRedirect(reverse_lazy("academica:"))


class NuevoHorario(generic.DetailView):
    model = HorarioDocente
    template_name='Horarios/Horarios_crear.html'
    context_object_name = "obj"
    form_class = nuevoHorarioform
    success_url = reverse_lazy("academica:crear_horario")
    login_url = "bases:login"

    def get(self, request, *args, **kwargs):
        fechaActual = datetime.datetime.now()
        fecha = fechaActual.date()
        year = fecha.strftime("%Y")
        month = fecha.strftime("%m")
        print("--------mes: ", month)
        print("--------año: ", year)
        query = Horario.objects.last()
        print("----query: ", query)
        if query == None:
            idorden = False
        else:
            idorden = query.Horario

        ordenes = Horario.objects.filter(
            fechaRecoleccion__year=year, fechaRecoleccion__month=month)
        #print("----ordenes: ", ordenes)
        #print("...idorden: ", idorden)

        context = {
            'idorden': idorden,
            'ordenes': ordenes
        }

        return render(request, 'nuevaorden.html', context)

    def post(self, request, *args, **kwargs):

        form = nuevoHorarioform(request.POST or None)

        if (request.POST and form.is_valid()):
            form.instance.uc = self.request.user
            query = Horario.objects.last()
            print("-------query: ", query)
            if query:
                idorden = int(query.Horario
                ) + 1
            else:
                idorden = 1

            form.instance.Horario = idorden
            form.save()

            fechaActual = datetime.datetime.now()
            fecha = fechaActual.date()
            year = fecha.strftime("%Y")
            month = fecha.strftime("%m")
            ordenes = Horario.objects.filter(
                fechaRecoleccion__year=year, fechaRecoleccion__month=month)
            context = {
                'idorden': idorden,
                'ordenes': ordenes
            }
            return render(request, 'Horario/Horario_list.html', context)
        else:
            context = {'form': form}
            return render(request, 'Horario/Horario_list.html', context)
class listHorarioView(LoginRequiredMixin, ValidatePermissionRequiredMixin, generic.ListView):
    model = Horario
    template_name = "Horarios/horario_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
