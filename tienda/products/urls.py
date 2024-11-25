
from .views import CategoryViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('products', ProductViewSet,basename='products')

urlpatterns = router.urls


# Django REST Framework proporciona otro sistema para definir las rutas de la API, que es más simple y directo.
# urlpatterns = [
#     path('products/', ProductList.as_view(), name='product-list'),
#     path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
# ]