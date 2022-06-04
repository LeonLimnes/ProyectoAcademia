from django.urls import path
from django.urls.resolvers import URLPattern
from .views import AcademicaView,listar_usuario_cliente, search ,GrupoView , GrupoDel, GrupoEdit, GrupoNew, GrupoView, HorarioView, HorarioNew, HorarioDel, HorarioEdit, registroPdf, registroView, registroNew, salidadocente, CrearHorarioView,listHorarioView,DocenteNew, DocenteView, DocenteEdit, DocenteDel
from django.contrib import admin  
from academica import views  
from django.conf.urls import url


urlpatterns = [
    path('academiaca/', AcademicaView.as_view(), name="academica_list"),
    #docente
    path('docente_list/', DocenteView.as_view(), name="docente_list"),
    path('docente/new/', DocenteNew.as_view(), name="docente_new"),
    path('docente/edit/<int:pk>', DocenteEdit.as_view(), name="docente_edit"),
    path('docente/delete/<int:pk>', DocenteDel.as_view(), name="docente_del"),
   
    #Rutas para horarios
    path('Horario_list/', HorarioView.as_view(), name="Horario_list"),
    path('Horario/new/', HorarioNew.as_view(), name="Horario_new"),
    path('Horario/edit/<int:pk>', HorarioEdit.as_view(), name="Horario_edit"),
    path('Horario/delete/<int:pk>', HorarioDel.as_view(), name="Horario_del"),

   #Rutas para grupo
    path('grupo_list/', GrupoView.as_view(), name="grupo_list"),
    path('grupo/new/', GrupoNew.as_view(), name="grupo_new"),
    path('grupo/edit/<int:pk>', GrupoEdit.as_view(), name="grupo_edit"),
    path('grupo/delete/<int:pk>', GrupoDel.as_view(), name="grupo_del"),

    #Rutas para registro
    path('registro_list/', registroView.as_view(), name="registro_list"),
    path('registro/new/', registroNew.as_view(), name="registro_new"),
    path('docente/sale/<int:pk>', salidadocente.as_view(), name="docente_sale"),
    path('registro_PDF/', registroPdf.as_view(), name="registro_PDF"),
    
    #Rutas para crear el horrio
    path('list_horarios/', listHorarioView.as_view(), name="list_horario"),
    path('new_horarios/', CrearHorarioView.as_view(), name="crear_horario"),
    


    path('admin/', admin.site.urls),  
    url(r'^search/$', views.search, name='search'),
    
]