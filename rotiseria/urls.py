from django.urls import path
from .View.principal import index
from rotiseria.View.Administrador import CrearProducto, ListarProducto, BorrarProducto,EditarProducto
urlpatterns = [

path('', index, name='index'),
path('crearproducto',CrearProducto.as_view(), name = 'crear_producto'),
path('listarproducto',ListarProducto.as_view(), name = 'listar_producto'),
path('borrar/producto/<str:nombrep>/', BorrarProducto, name='borrar_producto'),
path('editar/producto/<str:nombrep>/', EditarProducto, name='editar_producto'),
]