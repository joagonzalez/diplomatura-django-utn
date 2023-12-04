from django.db import models
from django.contrib.auth.models import User


class DatosUsuarios(models.Model):
    """
    Extiendo atributos de usuarios de django, a traves de FK
    usuarios
    """
    usuario = models.OneToOneField(User, blank=False, null=True, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="producto/%Y/%m/%d", default="defecto/defecto.png", blank=True, null=True)
    email = models.CharField(max_length=100, blank=False, null=False, default='johndoe@gmail.com')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    pais = models.CharField(max_length=30, blank=True)
    provincia = models.CharField(max_length=40, blank=True)
    ciudad = models.CharField(max_length=40, blank=True)
    domicilio = models.CharField(max_length=80, blank=True)
    celular = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return self.usuario.username
        


