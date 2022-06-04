from django.db import models
from django.shortcuts import redirect, HttpResponseRedirect
from datetime import datetime
from django.urls import reverse_lazy
from django.contrib import messages
from crum import get_current_request
'''class ValidatePermissionRequiredMixin(object):
    permission_required = ''
    url_redirect = None

    def get_perms(self):
        if isinstance(self.permission_required, str):
            perms = (self.permission_required, )
        else:
            perms = self.permission_required
        print("*****Permisos requeridos: ", perms)
        return perms

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('bases:home')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(self.get_perms()):
            return super().dispatch(request, *args, **kwargs)
        messages.error(request,'No Tiene Permisos Para Ingresar a Este Modulo')
        return HttpResponseRedirect(self.get_url_redirect())'''


class ValidatePermissionRequiredMixin(object):
    permission_required = ''
    url_redirect = None

    def get_perms(self):
        perms = []
        if isinstance(self.permission_required, str):
            perms.append(self.permission_required)
        else:
            perms = list(self.permission_required)
        return perms

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('bases:home')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):

        request = get_current_request()

        # El super Usuario no necesiota validar permisos
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        if 'group' in request.session:
            group = request.session['group']
            if not group:
                group = models.Group.objects.first()
            #print("******Group: ", group)
            perms = self.get_perms()
            for p in perms:
                print("p: ", p)
                if not group.permissions.filter(codename=p):
                    messages.error(
                        request, 'No Tiene Permisos Para Ingresar a Este Modulo')
                    return HttpResponseRedirect(self.get_url_redirect())
            return super().dispatch(request, *args, **kwargs)
        messages.error(
            request, 'No Tiene Permisos Para Ingresar a Este Modulo')
        return HttpResponseRedirect(self.get_url_redirect())