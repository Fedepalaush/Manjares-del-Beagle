from django.urls import path
from . import views

app_name = 'carro'

urlpatterns = [
    path('', views.carro_detail, name='carro_detail'),
    path('agregar/<int:pk>/', views.añadir_carrito, name='añadir_carrito'),
    path('borrar/<int:pk>/', views.remover_carrito, name='remover_carrito'),
]