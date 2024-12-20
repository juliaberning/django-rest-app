# Generated by Django 5.1.3 on 2024-11-26 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='imagen_default.png', upload_to='products/', verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='product',
            name='price_type',
            field=models.CharField(choices=[('unitario', 'Precio unitario'), ('media-doc', 'Precio por media docena'), ('docena', 'Precio por docena'), ('kilo', 'Precio por kilo')], default='unitario', max_length=20, verbose_name='Tipo de precio'),
        ),
    ]
