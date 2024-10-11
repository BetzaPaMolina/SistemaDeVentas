from django.db import models
from bases.models import ClaseModelo
# Create your models here.

class Categoria(ClaseModelo): #Hereda las propiedades/atributos de la clase models.model
    #django crea el id automaticamente
    descripcion = models.CharField( #especificamos las propiedades
        max_length=100,
        help_text='Descripción de la categoría',
        unique=True
    )
     
    def __str__(self): #metodo para mostrar la descripcion en el admin
        return '{}'.format(self.descripcion)
    
    def save(self): #sobreescribimos el metodo save para que la descripcion se guarde en mayusculas
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta: #metaclase para definir los atributos de la clase
        verbose_name_plural = "Categorías"