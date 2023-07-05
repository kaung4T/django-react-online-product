from django.urls import path, include
from application import views

urlpatterns = [
    path('', views.Home().index, name="index"),
    path('api', views.ProductApi.as_view(), name="api")
]
