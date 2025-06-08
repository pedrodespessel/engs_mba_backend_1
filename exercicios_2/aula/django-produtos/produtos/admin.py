from django.contrib import admin
from produtos.models import Product

# Register your models here.


admin.site.site_header = 'Administração de Produtos - MBA'
admin.site.register(Product)
