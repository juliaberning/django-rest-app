from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Filtrar productos por categoría
    # http://127.0.0.1:8000/api/products/?category=3
    def get_queryset(self):
        queryset =  super().get_queryset()

        # Filtado por categoría
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        
        # Filtado por nombre de producto
        search = self.request.query_params.get('search', None)
        if search: 
            queryset = queryset.filter(name__icontains=search)
        
        return queryset

    # Filtrar productos por categoría
    # http://127.0.0.1:8000/api/products/by_category/?Category=1
    # @action(detail=False)
    # def by_category(self, request):
    #     category = self.request.query_params.get('Category', None)
    #     products = Product.objects.filter(category=category)
    #     serializer = ProductSerializer(products, many=True)
    #     return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Se puede usar un viewset (más flexible) en lugar de generics
# class ProductList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
