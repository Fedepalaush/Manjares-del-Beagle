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

#Vista del carrito donde se definen varios metodos importantes
class VistaCarrito(View):

    def obtenerCarrito(request):
        #Si la 
        if 'alimentos' not in request.session:
            HttpResponseRedirect('/')

        else:

            form = ProductoIDForm()
            alimentos = request.session['alimentos']
            print (alimentos)
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
                print ('form valido')
                nombreApellido = form.cleaned_data['nombreApellido']
                celular = form.cleaned_data['celular']
                descripcion = form.cleaned_data['descripcion']
                direccion = form.cleaned_data['direccion']
                latitud = form.cleaned_data['latitud']
                longitud = form.cleaned_data['longitud']
                #Obtenemos solo la direccion con el numero, nada mas...
                direcccionActual = VistaCarrito.obtenerDireccion(direccion)
                print (direcccionActual)
                estaEnbd = False
                if direccionActual == " ": #Si la direccion es vacia es xq retira en la rotiseria
                    direccionActual = Mapa.objects.get(direccion = 'Belgrano 43')
                else:
                    #Si la direccion esta cargada en el modelo mapa, lo traemos y hacemos la relacion de pedido con mapa 
                    direciones = Mapa.objects.all()
                    for d in direcciones:
                        if d == direccionActual:
                            direccionActual = d
                            estaEnbd = True
                    if estaEnbd == False:
                        direccionActual = Mapa.objects.create(latitud = latitud, longitud = longitud, direccion = direccionActual)
                        direccionActual.save()
            alimentos = request.session['alimentos']
            bloque = Bloque.objects.get(id = 1)
            estadoPedido = EstadoPedido.objects.get(estado = 'pendiente')
            pedido = Pedido.objects.create(bloque = bloque, nombre_cliente = nombreApellido, estadoPedido = estadoPedido, descripcion = descripcion, telefono_cliente = celular, mapa = direccionActual)
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

    def obtenerDireccion(direccion):
        i = 0
        d = ' '
        if direccion != '-':
            while direccion[i] != ',':
                d = d + direccion[i]
                i = i + 1
        return d