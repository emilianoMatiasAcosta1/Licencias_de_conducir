from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from Licencia.models import Licencias
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView   


def indice(request):
    return render(request , 'Licencia/indice.html')


class LicenciasList(ListView):
    model = Licencias 
    context_object_name = 'usuario'


class LicenciasDetail(DetailView):
    model = Licencias
    context_object_name = 'usuario'


class LicenciasUpdate(UpdateView):
    model = Licencias 
    success_url = reverse_lazy('licencia-lista')
    fields = ['motivo']


class LicenciasDelete(DeleteView):
    model = Licencias
    context_object_name = 'usuario'
    success_url = reverse_lazy('licencia-lista')


class LicenciasCreate(CreateView):
    model = Licencias
    fields = '__all__'  
    success_url = reverse_lazy('licencia-lista')


class LicenciasSearch(ListView):
    model = Licencias
    context_object_name = 'usuario'

    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        resultado = (Licencias.objects.filter(documento__icontains=criterio).all())
        return resultado
    





                
                
                
                
                
                
                
                
                
                
                # Usando clases recibimos request, pero como estamos con objetos utilizamos el SELF para hacer referencia a ese objeto 
                # Seria una peticion que adentro tiene un request 
                
                # criterio = self.request.GET.get("criterio") | GET= el metodo para traer la request      get= para buscar si coincide alguan key en el diccionario criterio
                # El 'criterio' es por que a nuestro formulario le pusimos el nombre ese 
                # GET estamos utilizando en nuestro formulario (cargado en el index)
                
                # result = (Licencia.objects.filter(documento=criterio).all())
                # En esta linea, que en todos los objetos filtre lo que coincida con criterio
                # Tenemos que direccionar el action=''  , para la url creada para buscar  
                



        
    


