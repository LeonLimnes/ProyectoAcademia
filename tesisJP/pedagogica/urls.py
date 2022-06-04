from django.urls import path
from django.urls.resolvers import URLPattern


from .views import PlanView, CrearPlan, EliminarPlan, EditarPlan


urlpatterns = [
    path('plan/', PlanView.as_view(),name="plan_list"),
    path('plancrear/', CrearPlan.as_view(),name='plan_new'),
    path('editarplan/<int:pk>', EditarPlan.as_view(),name="plan_editar"),
    path('eliminarplan/<int:pk>', EliminarPlan.as_view(),name="plan_eliminar"),

]
