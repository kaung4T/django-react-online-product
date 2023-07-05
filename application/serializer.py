from rest_framework import serializers
from application.models import Product
from rest_framework.fields import CurrentUserDefault

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'user', 'user2', 'name', 'price']





    # def save(self):
    #     user = serializers.CurrentUserDefault()  # <= magic!
    #     user2 = [serializers.CurrentUserDefault()]
    #     name = self.validated_data['name']
    #     price = self.validated_data['price']
    def create(self, validated_data):

        print(self.context["request"].user)
        cust_req_data = {'user': self.context["request"].user,
                         'user2': [self.context["request"].user], 
                         'name': validated_data['name'],
                         'price': validated_data['price']
                        }

        data = ProductSerializer(data=cust_req_data)
        if data.is_valid():
            data.save()

        return Product.objects.create(**validated_data)
