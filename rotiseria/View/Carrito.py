from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import json as simplejson
from rotiseria.models import Producto
from rotiseria.forms import PedidoAlimentoForm, ProductoIDForm, ProductoIDForm
from django.shortcuts import get_object_or_404

class VistaCarrito(View):

    def obtenerCarrito(request):

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
                print ('formulario valido')
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
