from django.db import models

# Modelo de categorías
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']

    def __str__(self):
        return self.name

# Modelo de productos
class Product(models.Model):
    price_type_choices = (
        ('unitario', 'Precio unitario'),
        ('media-doc', 'Precio por media docena'),
        ('docena', 'Precio por docena'),
        ('kilo', 'Precio por kilo'),
    )
    name = models.CharField(max_length=255, verbose_name='Nombre')
    image = models.ImageField(upload_to='products/', default= 'imagen_default.png', verbose_name='Imagen')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='get_products', verbose_name='Categoría')
    description = models.TextField(verbose_name='Descripción')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    price_type = models.CharField(max_length=20, choices=price_type_choices, default='unitario', verbose_name='Tipo de precio')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['name']

    def __str__(self):
        return self.name
