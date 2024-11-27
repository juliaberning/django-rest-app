from rest_framework import serializers
from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    # Serializers no permiten acceder a campos de otros modelos directamente, 
    # por lo que se hace una referencia a través de un campo de solo lectura
    category_name = serializers.ReadOnlyField(source='category.name') 
    price_type_description = serializers.ReadOnlyField(source='get_price_type_display')   
    class Meta:
        model = Product
        # fields = ('id', 'name', 'description', 'price') # Para incluir solo los campos especificados en orden seleccionado
        fields = '__all__' # Para incluir todos los campos del modelo en orden de declaración

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'