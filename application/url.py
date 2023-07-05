from django.urls import path, include
from application import views

urlpatterns = [
    path('', views.Home().index, name="index"),
    path('api', views.ProductApi.as_view(), name="api"),
    path('api/update/<str:id>', views.ProductApi.as_view(), name="update"),
    path('api/delete/<str:id>', views.ProductApi.as_view(), name="delete"),
]
