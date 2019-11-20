from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import json as simplejson
from rotiseria.models import Producto, Bloque, Pedido, EstadoPedido, Cliente, PedidoProducto, Mapa
from rotiseria.forms import PedidoAlimentoForm, ProductoIDForm, ProductoIDForm, DatosClienteForm
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
import mercadopago
import json

mp = mercadopago.MP("2976477610493912", "36kgwdIqyhQeJylWXK8ftz692RzBWIYg")

#Vista del carrito donde se definen varios metodos importantes
class VistaCarrito(View):

    def obtenerCarrito(request):
        p = Pedido.objects.all()
        longitud = len(p)

        ultimo_pedido = p[longitud-1]

        preference = {
            "items": [
                {
                    "title": "Manjares del Beagle",
                    "quantity": 1,
                    "currency_id": "ARS",
                    "unit_price": float(ultimo_pedido.total)
                }
            ]
        }
        preferenceResult = mp.create_preference(preference)

        #Si la 
        if 'alimentos' not in request.session:
            HttpResponseRedirect('/')

        else:

            form = ProductoIDForm()
            alimentos = request.session['alimentos']
            lista = []
            total = 0
            #datos[0] -> id alimentoCarta // datos[1] -> cantidad
            for alimentoID, datos  in alimentos.items():
                alimento=get_object_or_404(Producto, id = int(alimentoID))
                subtotal = getattr(alimento, 'precioActual')*datos[1]
                lista.append({'alimentoID': alimento.id,
                            'alimentoNombre': alimento.nombre,
                            'precio': alimento.precioActual,
                            'cantidad': datos[1],
                            'subtotal': subtotal})
                total += subtotal

            return render(request, "Cliente/carrito.html", {
                'form'  : form,
                'lista' : lista,
                'total' : total,
                'preference_id' : json.dumps(preferenceResult['response']['id']),
            }) 

    def agregarItem(request):

        if request.method == 'POST':
            form = PedidoAlimentoForm(request.POST)
            if form.is_valid():
                contenido = {
                    'alimentoID' : form.cleaned_data['alimento'],
                    'cantidad' : form.cleaned_data['cantidad']
                }
                request.session['items'] = request.session['items'] + contenido['cantidad']
                if  contenido['alimentoID'] in request.session['alimentos']:
                        cant = request.session['alimentos'][contenido['alimentoID']][1]
                        request.session['alimentos'][contenido['alimentoID']][1] = contenido['cantidad'] + cant
                else :
                        request.session['alimentos'][contenido['alimentoID']] = contenido['alimentoID'], contenido['cantidad']

        return HttpResponseRedirect('/')

    def eliminarItem(request):

        if request.method == 'POST':
            form = ProductoIDForm(request.POST)
            if form.is_valid():
                id = form.cleaned_data['alimento']
                request.session['items'] = request.session['items'] - request.session['alimentos'][str(id)][1]
                request.session['alimentos'].pop(str(id),None)
                return HttpResponseRedirect('/carrito')

    @csrf_protect
    def confirmarPedido(request):

        if request.method == 'POST':
            form = DatosClienteForm(request.POST)
            if form.is_valid():
                nombreApellido = form.cleaned_data['nombreApellido']
                celular = form.cleaned_data['celular']
                descripcion = form.cleaned_data['descripcion']
                dire = form.cleaned_data['direccion']
                latitud = form.cleaned_data['latitud']
                longitud = form.cleaned_data['longitud']
                #Obtenemos solo la direccion con el numero, nada mas...
                direccion = VistaCarrito.obtenerDireccion(dire)
                descripcion = VistaCarrito.obtenerDescripcion(descripcion)
                estaEnbd = False
                if direccion == '': #Si la direccion es vacia es xq retira en la rotiseria
                    direccionCliente = Mapa.objects.get(direccion = 'General Manuel Belgrano 43')
                else:
                    #Si la direccion esta cargada en el modelo mapa, lo traemos y hacemos la relacion de pedido con mapa 
                    direcciones = Mapa.objects.all()
                    for d in direcciones:
                        if d.direccion == direccion:
                            direccionCliente = d
                            estaEnbd = True
                    if estaEnbd == False:
                        direccionCliente = Mapa.objects.create(latitud = latitud, longitud = longitud, direccion = direccion)
                        direccionCliente.save()
            alimentos = request.session['alimentos']
            bloque = Bloque.objects.get(id = 1)
            estadoPedido = EstadoPedido.objects.get(estado = 'pendiente')
            pedido = Pedido.objects.create(bloque = bloque, nombre_cliente = nombreApellido, estadoPedido = estadoPedido, descripcion = descripcion, telefono_cliente = celular, mapa = direccionCliente)
            total = 0
            #datos[0] -> id alimento // datos[1] -> cantidad de alimentos
            for alimentoID, datos  in alimentos.items():
                producto = Producto.objects.get(id = int(alimentoID))
                subtotal = getattr(producto, 'precioActual')*datos[1]
                total += subtotal
                precioActual = producto.precioActual
                pedidoProducto = PedidoProducto.objects.create(producto=producto, pedido=pedido,
                                                               precioVariable= precioActual, subtotal=subtotal,
                                                               cantidad=datos[1])
            pedido.total = total
            pedido.save()
            request.session.flush()

        return HttpResponseRedirect('/')

    def obtenerDireccion(dire):
        i = 0
        d = ''
        if dire != '-':
            while dire[i] != ',':
                d = d + dire[i]
                i = i + 1
        return d

    def obtenerDescripcion(desc):
        if desc == '-':
            desc = ""
        return desc
    