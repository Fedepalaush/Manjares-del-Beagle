from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from rotiseria.models import Producto
from .cart import Carro
from .forms import AñadirProductoCarritoForm

@require_POST
def añadir_carrito(request, pk):
    carro = Carro(request)
    producto = Producto.objects.get(pk=pk)
    form = AñadirProductoCarritoForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        carro.añadir(producto, cantidad=cd['cantidad'], actualizar_cantidad=cd['actualizar']) 
    return redirect ('carro: carro_detail')

def remover_carrito(request, pk):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id = pk)
    carro.borrar(producto)
    return redirect('carro: carro_detail')

def carro_detail(request):
    carro = Carro(request)
    for item in carro:
        item['actualizar_cantidad_form'] = AñadirProductoCarritoForm(initial={'cantidad': item['cantidad'], 'actualizar': True})
    return render (request, 'carro/detail.html', {'carro': carro})
    
