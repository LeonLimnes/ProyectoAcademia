from django.urls import path
from django.urls.resolvers import URLPattern
from .views import UsuarioView,CrearUsuario,ActualizarUsuario,BorrarUsuario


urlpatterns = [
    path('usuario/', UsuarioView.as_view(), name="usuarios_list"),
    path('usuariocrear/', CrearUsuario.as_view(), name="usuarios_crear"),
    path('usuarioactualizar/<int:pk>', ActualizarUsuario.as_view(), name="usuarios_actualizar"),
    path('usuarioborrar/<int:pk>', BorrarUsuario.as_view(), name="usuarios_borrar"),  
  
]