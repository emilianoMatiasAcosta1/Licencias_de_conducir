"""Registro_Automotor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from Licencia.views import ( indice, LicenciasList, LicenciasDetail, LicenciasUpdate, 
LicenciasDelete, LicenciasCreate, LicenciasSearch, Login, SignUp, Logout, LicenciasMineList
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('licencia', indice, name='indice'),
    path('licencia/lista', LicenciasList.as_view(), name='licencia-lista'), 
    path('licencia/detalle/<pk>', LicenciasDetail.as_view(), name='licencia-detalle'),
    path('licencia/actualizar/<pk>', LicenciasUpdate.as_view(), name='licencia-actualizar'),
    path('licencia/borrar/<pk>', LicenciasDelete.as_view(), name='licencia-borrar'),
    path('licencia/crear', LicenciasCreate.as_view(), name='licencia-crear'),
    path('licencia/buscar', LicenciasSearch.as_view(), name='licencia-buscar'),
    path('login/', Login.as_view(), name='login'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('logout/', Logout.as_view(), name='logout'),
    path('licencia/lista/mine', LicenciasMineList.as_view(), name='licencia-mine')
]
