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

class SubCategoria(ClaseModelo):
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la subcategoría'
    )

    def __str__(self):
        return '{}:{}'.format(self.Categoria.descripcion, self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save() 

    class Meta:
        verbose_name_plural = "Sub Categorías"
        unique_together = ('Categoria', 'descripcion')

class Marca(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la marca',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()

    class Meta:
        verbose_name_plural = "Marca"

class UnidadMedida(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la unidad de medida',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(UnidadMedida, self).save()

    class Meta:
        verbose_name_plural = "Unidades de Medida"