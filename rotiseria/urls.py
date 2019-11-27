from django.urls import path
<<<<<<< HEAD
from rotiseria.View.Administrador import CrearProducto, ListarProducto, BorrarProducto,EditarProducto, CrearCategoria, ListarCategorias, BorrarCategoría, index, indexAdministrador, indexProductos
from rotiseria.View.Recepcionista import CrearBloque, ListarBloque, BorrarBloque, ListarPedido, pedidosConfirmados, confirmar_pedido, rechazar_pedido, pedidosRechazados
from rotiseria.View.Cliente import CrearCliente, ListarCliente, BorrarCliente, CrearPedido, indexCliente, quienesSomos
=======
from rotiseria.View.Administrador import CrearProducto, ListarProducto, BorrarProducto, CrearCategoria, ListarCategorias, BorrarCategoría, index, indexAdministrador,  editarproducto
from rotiseria.View.Recepcionista import CrearBloque, ListarBloque, BorrarBloque
from rotiseria.View.Cliente import CrearCliente, ListarCliente, BorrarCliente, CrearPedido, ListarPedido, indexCliente, quienesSomos
>>>>>>> ab2d911e7e35b14c884f99909a88e55e0600df00
from rotiseria.View.Repartidor import ListarDatosMapa
from rotiseria.View.Sesion import SignIn, register, login
from rotiseria.View.Carrito import VistaCarrito
from django.contrib.auth.views import logout_then_login

urlpatterns = [
path('indexAdministrador',indexAdministrador, name = 'index_administrador'),

path( 'editarProducto/<int:id_producto>', editarproducto, name = 'editar_producto'),
path('crear_Producto',CrearProducto.as_view(), name = 'crear_producto'),
path('listarProductos',ListarProducto.as_view(), name = 'listar_producto'),
path('borrarProducto/<str:nombrep>/', BorrarProducto, name='borrar_producto'),


path('crearCategoría',CrearCategoria.as_view(), name = 'crear_categoria'),
path('listarCategorías',ListarCategorias.as_view(), name = 'listar_categoria'),
path('borrarCategoría/<str:nombrec>/', BorrarCategoría, name='borrar_categoria'),

path('crearBloque',CrearBloque.as_view(), name = 'crear_bloque'),
path('listarBloques',ListarBloque.as_view(), name = 'listar_bloque'),
path('borrarBloque/<int:id>/', BorrarBloque, name='borrar_bloque'),


path('crearCliente',CrearCliente.as_view(), name = 'crear_cliente'),
path('listarClientes',ListarCliente.as_view(), name = 'listar_cliente'),
path('borrarCliente/<int:dni>/', BorrarCliente, name='borrar_cliente'),

path('', indexCliente, name='indexCliente'),
path('indexUsuario', index, name = "indexUsuario"),
path('crearPedido',CrearPedido.as_view(), name = 'crear_pedido'),

# Urls del recepcionista
path('recepcionista',ListarPedido.as_view(), name = 'listar_pedidos'),
path('pedidosConfirmados', pedidosConfirmados, name = 'pedidos_confirmados'),
path('pedidosRechazados', pedidosRechazados, name = 'pedidos_rechazados'),
path('confirmar_pedido/<int:id>/', confirmar_pedido, name = 'confirmar_pedido'),
path('rechazar_pedido/<int:id>/', rechazar_pedido, name = 'rechazar_pedido'),

path('quienesSomos',quienesSomos, name = 'quienesSomos'),

path('vistaMapa',ListarDatosMapa.as_view(), name = 'listar_datos_mapa'),
#iniciar sesion
path('accounts/login/',login, name = 'login'),
#cerrar sesion
path('logout/',logout_then_login, name = 'logout'),
path('registro',register, name = 'registro'),

#URLs para operar con el carrito de compras
path('carrito', VistaCarrito.obtenerCarrito, name = "carrito"),
path('agregaritem', VistaCarrito.agregarItem, name = "agregaritem"),
path('eliminarItem', VistaCarrito.eliminarItem, name = "eliminarItem"),
path('confirmarPedido', VistaCarrito.confirmarPedido, name = "confirmarPedido"),
]