from django.urls import path
from django.urls.resolvers import URLPattern
from .views import PlanView, CrearPlan 


urlpatterns = [
    path('plan/', PlanView.as_view(),name="plan_list"),
    path('crearplan/', CrearPlan.as_view(),name='plan_new'),
    #path('planew/', PlanNew.as_view(),name="plan_new"),
  
]
