from django import forms 
from Licencia.models import Licencias

class Licencias(forms.ModesForm):
    class Meta:
        model = Licencias 
        fields = ['nombre','apellido','documento']




# Aqui tenems la clase forumulario con todo lo que necesitamos en nuestros formularis 
