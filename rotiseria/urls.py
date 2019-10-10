from django.urls import path
from .View.principal import index
from rotiseria.View.Administrador import CrearProducto, ListarProducto, BorrarProducto,EditarProducto, CrearCategoria, ListarCategorias, BorrarCategoría
from rotiseria.View.Recepcionista import CrearBloque, ListarBloque, BorrarBloque
from rotiseria.View.Cliente import CrearCliente, ListarCliente, BorrarCliente, CrearPedido, ListarPedido
urlpatterns = [

path('', index, name='index'),
path('crear_Producto',CrearProducto.as_view(), name = 'crear_producto'),
path('listarProductos',ListarProducto.as_view(), name = 'listar_producto'),
path('borrarProducto/<str:nombrep>/', BorrarProducto, name='borrar_producto'),
path('editarProducto/<str:nombrep>/', EditarProducto, name='editar_producto'),

path('crearCategoría',CrearCategoria.as_view(), name = 'crear_categoria'),
path('listarCategorías',ListarCategorias.as_view(), name = 'listar_categoria'),
path('borrarCategoría/<str:nombrec>/', BorrarCategoría, name='borrar_categoria'),

path('crearBloque',CrearBloque.as_view(), name = 'crear_bloque'),
path('listarBloques',ListarBloque.as_view(), name = 'listar_bloque'),
path('borrarBloque/<int:id>/', BorrarBloque, name='borrar_bloque'),


path('crearCliente',CrearCliente.as_view(), name = 'crear_cliente'),
path('listarClientes',ListarCliente.as_view(), name = 'listar_cliente'),
path('borrarCliente/<int:dni>/', BorrarCliente, name='borrar_cliente'),


path('crearPedido',CrearPedido.as_view(), name = 'crear_pedido'),
path('listarPedidos',ListarPedido.as_view(), name = 'listar_pedidos'),
]