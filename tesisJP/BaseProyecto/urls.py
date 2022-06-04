"""BaseProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include(('bases.urls', 'bases'), namespace='bases')),
    path('pedagogica/', include(('pedagogica.urls', 'pedagogica'), namespace='pedagogica')),
    path('pedagogica/axis/', include('pedagogica.axis.urls')),
    path('pedagogica/subject/', include('pedagogica.subject.urls')),
    path('pedagogica/major/', include('pedagogica.major.urls')),
    path('pedagogica/roadmap/', include('pedagogica.roadmap.urls')),
    path('academica/', include(('academica.urls', 'academica'), namespace='academica')),
    path('usuarios/', include(('usuarios.urls', 'usuarios'), namespace='usuarios')),

    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
