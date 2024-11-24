from rest_framework import serializers
from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ('id', 'name', 'description', 'price') # Para incluir solo los campos especificados en orden seleccionado
        fields = '__all__' # Para incluir todos los campos del modelo en orden de declaración

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'