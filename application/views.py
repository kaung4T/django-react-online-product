from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

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

        return Response()


