from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True) # todo registro es "true por defecto"
    fc = models.DateTimeField(auto_now_add=True) # fecha de creacion
    fm = models.DateTimeField(auto_now=True) # fecha de modificacion
    uc = models.ForeignKey(User, on_delete=models.CASCADE) # usuario creador
    um = models.IntegerField(blank = True, null = True) # usuario modificador

    class Meta:
        abstract = True #ya no toma en cuenta esta clase como un modelo de la base de datos