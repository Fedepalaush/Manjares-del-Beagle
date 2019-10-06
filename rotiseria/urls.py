from django.urls import path
from .View.principal import index
from rotiseria.View.Administrador import CrearProducto, ListarProducto
urlpatterns = [

path('', index, name='index'),
path('crearproducto',CrearProducto.as_view(), name = 'crear_producto'),
path('listarproducto',ListarProducto.as_view(), name = 'listar_producto'),
]