from django.db import models
from django.contrib.auth.models import User 

MOTIVO_NUEVO = 'Nuevo'
MOTIVO_RENOVACION = 'Renovacion'
MOTIVO_AMPLIACION = 'Ampliacion'

MOTIVO = [
    (MOTIVO_NUEVO,'Nuevo'),
    (MOTIVO_RENOVACION,'Renovacion'),    
    (MOTIVO_AMPLIACION,'Ampliacion'),
] 

class Licencias(models.Model):                                                                           # Heredamos propiedades del model
    nombre = models.CharField(max_length=100)
    apellido =  models.CharField(max_length=100)
    documento =  models.CharField(max_length=100)
    motivo =  models.CharField(max_length=100, choices=MOTIVO, default= MOTIVO_NUEVO)
    foto = models.ImageField(null=True, blank=True , upload_to='mi_licencia')
    id_usuario = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='id_usuario')



    def __str__(self):
        return (f'{self.nombre} {self.apellido} {self.documento} ')    
    

    

    # licencia / licencia123
