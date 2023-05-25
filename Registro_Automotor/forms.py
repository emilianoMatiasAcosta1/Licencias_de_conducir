from django import forms
from Licencia.models import Licencias 



class LicenciasForm(forms.ModelForm):
    class Meta: 
        model = Licencias
        fields = '__all__'