from rest_framework import serializers
from application.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'user', 'user2', 'name', 'price']
