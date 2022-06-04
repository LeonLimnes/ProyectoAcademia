import genericpath
import re
from django.views import generic
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import fields
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.utils.regex_helper import Group
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from .models import Roadmap, Perfil_Egreso, Ambitos, Major, Semester, Axis, Subject, Competencias, Complementarias, Firmas, Ambitos_Ingreso, Certificacion_Est, Certificacion, Procedimiento_Acre, Procedimiento_Eval, Procedimientos, Recomendaciones_Met, Recomendaciones, Subrecomendaciones, Perfil_Ingreso, Catalogo_Ejes
from .forms import PlanEstudioForm, Perfil_EgresoForm, AmbitosForm, CarreraForm, AnoForm, SemestreForm, EjesForm, AsignaturaForm, CompetenciasForm, ComplementariasForm, FirmasForm, Ambitos_IngresoForm, Certificacion_EstForm, CertificacionForm, Procedimiento_AcreForm, Procedimiento_EvalForm, ProcedimientosForm, Recomendaciones_MetForm, RecomendacionesForm, SubrecomendacionesForm, Perfil_IngresoForm, Catalogo_EjesForm

#############################################

from django.views.generic import View
from django.contrib.auth import models
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template

from django.contrib.staticfiles import finders
from xhtml2pdf import pisa



from django.contrib.auth.hashers import check_password

# Bibliotecas para la impresion del PDF
import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.template import Context
from django.template.loader import get_template
from django.conf.global_settings import MEDIA_URL, STATIC_URL



from .mixins import ValidatePermissionRequiredMixin



 




# Create your views here.



class PlanView(LoginRequiredMixin, generic.ListView):
    model =  Roadmap
    template_name= "p.html"
    context_object_name= "obj"
    login_url = "bases:login"

class CrearPlan(LoginRequiredMixin,ValidatePermissionRequiredMixin, generic.CreateView):
    model = Roadmap
    template_name= "crearplan.html"
    context_object_name= "obj"
    form_class = Perfil_EgresoForm
    second_form_class = CompetenciasForm
    third_form_class = AmbitosForm
    four_form_class=ComplementariasForm
    fift_form_class= Ambitos_IngresoForm
    six_form_class= Perfil_IngresoForm
    seven_form_class= CertificacionForm
    eight_form_class= Certificacion_EstForm
    nine_form_class= Procedimiento_AcreForm
    ten_form_class= FirmasForm
    eleven_form_class= ProcedimientosForm
    twelve_form_class= Procedimiento_EvalForm
    thirteen_form_class= SubrecomendacionesForm
    fourteen_form_class= RecomendacionesForm
    fifteen_form_class= Recomendaciones_MetForm
    sixteen_form_class= AsignaturaForm
    seventeen_form_class= EjesForm
    eighteen_form_class= SemestreForm
    nineteen_form_class= AnoForm
    twenty_form_class= CarreraForm
    thirty_form_class= PlanEstudioForm
    succes_url= reverse_lazy('pedagogica:plan_list')
    login_url = "bases:login"
    
    
    
    def get(self,request, *args, **kwargs):
        plan = Roadmap.objects.last()
        carrera= Major.objects.all()
        #ano = Ano.objects.all()
        semestre = Semester.objects.all()
        ejes = Axis.objects.all()
        asignatura= Subject.objects.all()
        nombreejes= Catalogo_Ejes.objects.all()

        #Creacion del contex 
        context= {
            'plan':plan,
            #'ano':ano,
            'carrera':carrera,
            'semestre':semestre,
            'ejes':ejes,
            'asignatura':asignatura,
            'nombreejes':nombreejes
        }   
        return render(request, 'crearplan.html', context)

    def get_context_data(self, **kwargs):
        context= super(CrearPlan, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(self.request.GET)
        if 'form4' not in context:
            context['form4'] = self.four_form_class(self.request.GET)
        if 'form5' not in context:
            context['form5'] = self.fift_form_class(self.request.GET)
        if 'form6' not in context:
            context['form6'] = self.six_form_class(self.request.GET)
        if 'form7' not in context:
            context['form7'] = self.seven_form_class(self.request.GET)
        if 'form8' not in context:
            context['form8'] = self.eight_form_class(self.request.GET)
        if 'form9' not in context:
            context['form9'] = self.nine_form_class(self.request.GET)
        if 'form10' not in context:
            context['form10'] = self.ten_form_class(self.request.GET)
        if 'form11' not in context:
            context['form11'] = self.eleven_form_class(self.request.GET)
        if 'form12' not in context:
            context['form12'] = self.twelve_form_class(self.request.GET)
        if 'form13' not in context:
            context['form13'] = self.thirteen_form_class(self.request.GET)
        if 'form14' not in context:
            context['form14'] = self.fourteen_form_class(self.request.GET)
        if 'form15' not in context:
            context['form15'] = self.fifteen_form_class(self.request.GET)
        if 'form16' not in context:
            context['form16'] = self.sixteen_form_class(self.request.GET)
        if 'form17' not in context:
            context['form17'] = self.seventeen_form_class(self.request.GET)
        if 'form18' not in context:
            context['form18'] = self.eighteen_form_class(self.request.GET)
        if 'form19' not in context:
            context['form19'] = self.nineteen_form_class(self.request.GET)
        if 'form20' not in context:
            context['form20'] = self.twenty_form_class(self.request.GET)
        if 'form30' not in context:
            context['form30'] = self.thirty_form_class(self.request.GET)
        return context

    def post (self, request, *args, **kwargs):
        
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        form3 = self.third_form_class(request.POST)
        form4 = self.four_form_class(request.POST)
        form5 = self.fift_form_class(request.POST)
        form6 = self.six_form_class(request.POST)
        form7 = self.seven_form_class(request.POST)
        form8 = self.eight_form_class(request.POST)
        form9 = self.nine_form_class(request.POST)
        form10 = self.ten_form_class(request.POST)
        form11 = self.eleven_form_class(request.POST)
        form12 = self.twelve_form_class(request.POST)
        form13 = self.thirteen_form_class(request.POST)
        form14 = self.fourteen_form_class(request.POST)
        form15 = self.fifteen_form_class(request.POST)
        form16 = self.sixteen_form_class(request.POST)
        form17 = self.seventeen_form_class(request.POST)
        form18 = self.eighteen_form_class(request.POST)
        form19 = self.nineteen_form_class(request.POST)
        form20 = self.twenty_form_class(request.POST)
        form30 = self.thirty_form_class(request.POST)

        if form2.is_valid() :
            competencia=form2.save()
            
            print("*******************************************competencia: " ,competencia.id)          
 
        if form3.is_valid():
            form3.instance.aCompetencia=competencia
            ambitos=form3.save()
            print("*******************************************ambitos: " ,ambitos.id)
        
        if form.is_valid():
            form.instance.ambito=ambitos
            perfilegreso=form.save()
            
            print("*******************************************perfil de egreso: " ,perfilegreso.id)
        
        if form4.is_valid():
            complementarias=form4.save()
            
            print("*******************************************complementarias: " ,complementarias.id)
        
        if form5.is_valid():
            ambitos_ingreso=form5.save()
            
            print("*******************************************ambitosingreso: " ,ambitos_ingreso.id)
        
        if form6.is_valid():
            form6.instance.aAmbitosIngreso=ambitos_ingreso
            perfilingreso=form6.save()
            
            print("*******************************************perfilingresoo: " ,perfilingreso.id)
        
        if form7.is_valid():
            certificacion=form7.save()
            
            print("*******************************************certificacion: " ,certificacion.id)
        if form8.is_valid():
            form8.instance.aCertificacion=certificacion
            certificadodeestudios=form8.save()
            
            print("*******************************************certificadodeestudios: " ,certificadodeestudios.id)
        if form9.is_valid():
            procedimientosacreditacion=form9.save()
            
            print("*******************************************procedimientosacreditacion " ,procedimientosacreditacion.id)
        if form10.is_valid():
            firmas=form10.save()
            
            print("*******************************************firmas " ,firmas.id)
        if form11.is_valid():
            procedimientosel=form11.save()
            
            print("*******************************************procedimientos " ,procedimientosel.id)
        
        if form12.is_valid():
            form12.instance.aProcedimientos=procedimientosel
            procedimientoevaluacion=form12.save()
            
            print("*******************************************procedimientos de evaluacion: " ,procedimientoevaluacion.id)
        if form13.is_valid():
            subrecomendaciones=form13.save()
            
            print("*******************************************subrecomendaciones " ,subrecomendaciones.id)
        if form14.is_valid():
            form14.instance.aSubRecomendaciones=subrecomendaciones
            recomendaciones=form14.save()
            
            print("*******************************************recomendaciones: " ,recomendaciones.id)
        if form15.is_valid():
            form15.instance.aProcedimientos=recomendaciones
            recomendacionesmet=form15.save()
            
            print("*******************************************recomendacionesmet: " ,recomendacionesmet.id)
        #if form16.is_valid():
         #   asignatura=form16.save()
          #  print("*******************************************asignatura " ,asignatura.id)
        
        if form17.is_valid() and form16.is_valid():
            print("+++++++++++++++++++++++++++++++++++++++++++ejes: ", form17)
        
        if form18.is_valid() and form16.is_valid():
            sem=form18.cleaned_data.get('semestre')
            asig=form16.cleaned_data.get('asignatura')

            
            objsem=Semester.objects.filter(id=sem)
            objasignatura=Subject.objects.filter(id=asig)

            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", asig)
            vejes =form17.cleaned_data.get('ejes')
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ejes:", vejes)
            
            for x in vejes:
                print("####################################", x )
                Catalogo_Ejes.objects.filter(id=x)
                form19.instance.asemestre=x
                ano=form19.save()
                form20.instance.aano =ano
                carrera=form20.save() 


      
                   
        

        if form30.is_valid():
            form30.instance.pCarrera=carrera
            form30.instance.descripcionPEgre=perfilegreso
            form30.instance.pComplementarias=complementarias
            form30.instance.pFirmas=firmas
            form30.instance.pPerfil_Ingreso=perfilingreso
            form30.instance.pCertificacion_Est=certificadodeestudios
            form30.instance.pProcedimiento_Acre=procedimientosacreditacion
            form30.instance.pProcedimiento_Eval=procedimientoevaluacion
            form30.instance.pRecomendaciones_Met=recomendacionesmet
            plandeestudio=form30.save()

            print("*******************************************plandeestudio: " ,plandeestudio.id)
            
        
            return HttpResponseRedirect(reverse_lazy('pedagogica:plan_list'))
           
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form16=form16, form17=form17))
       




class EditarPlan(LoginRequiredMixin, generic.UpdateView):
    model = Roadmap
    template_name= "crearplan.html"
    context_object_name= "obj"
    form_class = PlanEstudioForm
    login_url = "bases:login"
 
    def get(self, request, *args, **kwargs):
            # se indica en el formulario que se va a hacer un edit
            # Se obtiene ID del Doctor
            pk = self.kwargs['pk']

            form = Roadmap.objects.get(id=pk)
            # print("Grupos Edit: ", form.groups.all())
            # Obtiene los grupos existentes que no estan asignados al usuario
            carrera = Major.objects.all()
            # print("***GruposNoSeleccionados: ", gruposNoSeleccionados)
            # print("***GruposSeleccionados: ", form.groups.all())

            context = {'obj': form, 'edit': True, 'carrera':carrera}
            return render(request, 'crearplan.html', context)


        
 

class EliminarPlan(LoginRequiredMixin, generic.DeleteView):
    model = Roadmap
    template_name= "eliminarplan.html"
    context_object_name= "obj"
    success_url = reverse_lazy('pedagogica:plan_list')

