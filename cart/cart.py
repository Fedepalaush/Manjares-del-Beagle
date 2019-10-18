from decimal import Decimal
from django.conf import settings
from rotiseria.models import Producto

class Carro(object):

    def __init__(self, request):
        #Inicializacion del carrito
        self.session = request.session
        carro = self.session.get(settings.CART_SESSION_ID)
        if not carro:
            #Guardamos un carro vacio en la sesion
            carro = self.session[settings.CART_SESSION_ID] = {}
        self.carro = carro

    def añadir(self, producto, cantidad=1, actualizar_cantidad=False):
        #Añadir un producto al carrito o actualizar esta cantidad
        producto_id = (producto.nombre)
        if producto_id not in self.carro:
            self.carro[producto_id] = {'cantidad': 0, 'precio': str(producto.precioActual) }
        
        if actualizar_cantidad:
            self.carro[producto_id]['cantidad'] = cantidad
        else:
            self.carro[producto_id]['cantidad'] += cantidad
        self.save()

    def borrar(self, producto):
        #Remover producto del carrito
        producto_id = (producto.nombre)

        if producto_id in self.carro:
            del self.carro[producto_id]
            self.save()
    
    def save(self):
        #Actualizar la sesion del carrito
        self.session[settings.CART_SESSION_ID] = self.carro
        #Marque la session como modificada para asegurarse de qe se guarde.
        self.session.modified = True

    def __iter__(self):
        #Iterar sobre los items del carro y obtener los productos de la base de datos
        productos_id = self.carro.keys()
        #obtengo los objetos productos y lo agrego al carro
        productos = Producto.objects.filter(id__in=productos_id)
        for producto in productos:
            self.carro[producto.nombre]['producto'] = producto

        for item in self.carro.values():
            item['precio'] = Decimal(item['precio'])
            item['precio_total'] = item['precio'] * item['cantidad']
            yield item
    
    def __len__(self):
        #Cuenta todos los item del carro
        return sum(item['cantidad'] for item in self.carro.values())

    def clear(self):
        #Vaciar el carrito
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    def get_precio_total(self):
        return sum(Decimal(item['precio']) * item['cantidad'] for item in self.carro.values())
        
