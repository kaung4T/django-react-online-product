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
    def create(self, data):

        print(self.context["request"].user)
        cust_req_data = {'user': self.context["request"].user,
                         'user2': [self.context["request"].user], 
                         'name': data['name'],
                         'price': data['price']
                        }

        ps = ProductSerializer(data=cust_req_data)
        if ps.is_valid():
            ps.save()

        return Product.objects.create(**data)
