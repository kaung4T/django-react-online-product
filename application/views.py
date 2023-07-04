from django.shortcuts import render

# Create your views here.


class Home:
    def index(self, request):
        context = {
            "name": "django"
        }
        return render(request, 'index.html',
                    context)