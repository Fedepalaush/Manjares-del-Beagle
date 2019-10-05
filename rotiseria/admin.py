from django.contrib import admin

from rotiseria.models import bloque, categoría, cliente, estadopedido, pedido, pedidoproducto, producto, rol, usuario
admin.register(bloque)
admin.register(categoría)
admin.register(cliente)
admin.register(estadopedido)
admin.register(pedido)
admin.register(pedidoproducto)
admin.register(producto)
admin.register(rol)
admin.register(usuario)