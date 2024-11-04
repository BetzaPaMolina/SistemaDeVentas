from rest_framework import serializers
#modifique todo lo de cliente con relacion a urls, views y aqui
from inv.models import Producto
from fac.models import Cliente

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model=Producto
        fields='__all__'


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model=Cliente
        fields='__all__'