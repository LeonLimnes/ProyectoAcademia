import genericpath
from django.views import generic
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import fields
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.regex_helper import Group
from django.shortcuts import render

from pedagogica.models import Plan_Estudio, Ano, Carrera, Semestre, Ejes,Asignatura
from pedagogica.forms import PlanEstudioForm



# Create your views here.



class PlanView(LoginRequiredMixin, generic.ListView):
    model =  Plan_Estudio
    template_name= "p.html"
    context_object_name= "obj"
    login_url = "bases:login"

class CrearPlan(LoginRequiredMixin, generic.CreateView):
    model = Plan_Estudio
    template_name= "crearplan.html"
    context_object_name= "obj"
    form_class = PlanEstudioForm
    login_url = "bases:login"
    succes_url= reverse_lazy ("pedagogica:plan_list")
    
    def get(self, request, *args, **kwargs): 
        #Lo primero a buscar es saber si existe un plan de estudios o no 
        plan = Plan_Estudio.objects.last()
        carrera = Carrera.objects.last()
        ano = Ano.objects.last()
        semestre = Semestre.objects.last()
        ejes = Ejes.objects.last()
        asignatura= Asignatura.objects.last()
        if plan:
            print("---------------plan:", plan)
        else:
            print("---------------No hay plan registrado aun")
        if ano:
            print("---------------si hay año:", ano)
        else:
            print("---------------No hay año")
        if carrera:
            print("---------------si hay carreras:", carrera)
        else:
            print("---------------No hay carreras")
        if semestre:
            print("---------------si hay semestre:", semestre)
        else:
            print("---------------No hay semestre")
        if ejes:
            print("---------------si hay ejes:", ejes)
        else:
            print("---------------No hay ejes")
        if asignatura:
            print("---------------si hay asignatura:", asignatura)
        else:
            print("---------------No hay asignatura")
        
        #Creacion del contex 
        context={
            'plandeestudio':plan,
            'ano':ano,
            'carrera':carrera,
            'semestre':semestre,
            'ejes':ejes,
            'asignatura':asignatura,
        }   
        return render(request,'crearplan.html', context) 
     
    def post(self, request, *args, **kwargs):
        pass


