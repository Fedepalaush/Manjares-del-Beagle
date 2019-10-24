from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import json as simplejson
from rotiseria.models import Producto

class VistaCarrito(View):

    def verCarrito(request):
        alimentos = request.session['alimentos']
        lista = []
        for pk in alimentos.items():
            producto = Producto.objects.get(pk = pk)
            lista.append({
                'nombre': producto.nombre
            })
        return render (request, "Cliente/carrito.html", {'lista': lista})

    def añadirCarrito(request, pk):
        if producto not in request.session['alimentos']:
            request.session['alimentos'] =  request.session['alimentos'] + [producto]
        return render(request, 'Cliente/carrito.html')
