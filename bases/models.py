from django.db import models
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey

# Create your models here.
class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True) # todo registro es "true por defecto"
    fc = models.DateTimeField(auto_now_add=True) # fecha de creacion
    fm = models.DateTimeField(auto_now=True) # fecha de modificacion
    uc = models.ForeignKey(User, on_delete=models.CASCADE) # usuario creador
    um = models.IntegerField(blank = True, null = True) # usuario modificador

    class Meta:
        abstract = True #ya no toma en cuenta esta clase como un modelo de la base de datos

class ClaseModelo2(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    # uc = models.ForeignKey(User, on_delete=models.CASCADE)
    # um = models.IntegerField(blank=True,null=True)
    uc = UserForeignKey(auto_user_add=True,related_name='+') #anula el mapeo en reversa
    um = UserForeignKey(auto_user=True,related_name='+')

    class Meta:
        abstract=True