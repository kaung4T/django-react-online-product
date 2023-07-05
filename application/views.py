from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from application.models import Product
from application.serializer import ProductSerializer

# Create your views here.


class Home:
    def index(self, request):
        context = {
            "name": "django"
        }
        return render(request, 'index.html',
                    context)


class ProductApi(APIView):
    def get(self, request):
        product = Product.objects.all()
        ps = ProductSerializer(product, many=True)

        return Response(data=ps.data)

    def post(self, request):
        ps = ProductSerializer(data=request.data, context={'request': request})
        
        if ps.is_valid():

            ps.save()
            return Response(data=ps.data)
        return Response(data=ps.errors)

    def put(self, request, id):
        product = Product.objects.get(id=id)
        ps = ProductSerializer(product, data=request.data)
        if ps.is_valid():
            ps.save()
            return Response(data=ps.data)
        return Response(data=ps.errors)

    def delete(self, request, id):
        product = Product.objects.get(id=id)
        product.delete()
        return Response(data={"success": "success"})


