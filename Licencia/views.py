from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from Licencia.models import Licencias
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView   
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def indice(request):
    return render(request , 'Licencia/indice.html')


class LicenciasList(ListView):
    model = Licencias 
    context_object_name = 'usuario'


class LicenciasMineList(LoginRequiredMixin, LicenciasList):
    
    def get_queryset(self):
        return Licencias.objects.filter(id_usuario=self.request.user.id).all()


class LicenciasDetail(LoginRequiredMixin, DetailView):
    model = Licencias
    context_object_name = 'usuario'


class PermisoSoloDueño(UserPassesTestMixin):

    def test_func(self):                                                                        # Esto es una funcion que tiene que devolver un verdadero o un falso  
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk') 
        return Licencias.objects.filter(id_usuario=user_id, id=post_id).exists()
    

class LicenciasUpdate(LoginRequiredMixin,PermisoSoloDueño ,UpdateView):
    model = Licencias 
    success_url = reverse_lazy('licencia-lista')
    fields = ['motivo','id_usuario']

    
class LicenciasDelete(LoginRequiredMixin, PermisoSoloDueño, DeleteView):
    model = Licencias
    context_object_name = 'usuario'
    success_url = reverse_lazy('licencia-lista')


class LicenciasCreate(CreateView):
    model = Licencias
    fields = '__all__'  
    success_url = reverse_lazy('licencia-lista')


class LicenciasSearch(LoginRequiredMixin, ListView):
    model = Licencias
    context_object_name = 'usuario'

    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        resultado = (Licencias.objects.filter(documento__icontains=criterio).all())
        return resultado
    

class Login(LoginView):
    next_page = reverse_lazy('indice') 


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('licencia-lista')


class Logout(LogoutView):
    template_name = 'registration/logout.html'    



    
           
    





                
                
                
                
                
                
                
                
                
                
                # Usando clases recibimos request, pero como estamos con objetos utilizamos el SELF para hacer referencia a ese objeto 
                # Seria una peticion que adentro tiene un request 
                
                # criterio = self.request.GET.get("criterio") | GET= el metodo para traer la request      get= para buscar si coincide alguan key en el diccionario criterio
                # El 'criterio' es por que a nuestro formulario le pusimos el nombre ese 
                # GET estamos utilizando en nuestro formulario (cargado en el index)
                
                # result = (Licencia.objects.filter(documento=criterio).all())
                # En esta linea, que en todos los objetos filtre lo que coincida con criterio
                # Tenemos que direccionar el action=''  , para la url creada para buscar  
                



        
    


