from django.contrib import admin
from application.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'user2', 'name', 'price']




admin.site.register(Product)
