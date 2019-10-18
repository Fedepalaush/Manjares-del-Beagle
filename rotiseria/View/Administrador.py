from django.views.generic import CreateView, ListView
from django.shortcuts import render, redirect, HttpResponse
from rotiseria.models import Producto, Categoría
from rotiseria.forms import ProductoForm, CategoriaForm
from django.urls import reverse_lazy

def index(request):
    return render(request, 'base.html')

class CrearProducto (CreateView):
        model = Producto
        form_class= ProductoForm
        template_name = 'Administrador/crearproducto.html'
        success_url = reverse_lazy('index')

class ListarProducto (ListView):
    model = Producto
    template_name = "Administrador/listarproducto.html"
    form_class = ProductoForm

    def get(self, request, *args, **kwargs):
        productos = Producto.objects.all()
        context_dict = {'productos': productos}
        return render(request, self.template_name, context=context_dict)


def BorrarProducto(request, nombrep):
	producto = Producto.objects.get(nombre=nombrep)
	if request.method == 'POST':
		producto.delete()
		return redirect('index')
	return render(request, 'Administrador/borrarproducto.html', {'producto':producto})

def EditarProducto(request, nombrep):
    producto = Producto.objects.get(nombre=nombrep)
    if request.method == 'GET':
         form = ProductoForm(request.POST, instance= producto)
    else:
        form = ProductoForm (request.POST, instance = producto)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request, 'Administrador/crearproducto.html', {'form':form})

class CrearCategoria(CreateView):
        model = Categoría
        form_class = CategoriaForm
        template_name = 'Administrador/crearcategoria.html'
        success_url = reverse_lazy('index')

class ListarCategorias (ListView):
    model = Categoría
    template_name = "Administrador/listarcategorías.html"
    form_class = CategoriaForm

    def get(self, request, *args, **kwargs):
        categorías = Categoría.objects.all()
        context_dict = {'categorías': categorías}
        return render(request, self.template_name, context=context_dict)


def BorrarCategoría(request, nombrec):
	categoría = Categoría.objects.get(nombre=nombrec)
	if request.method == 'POST':
		categoría.delete()
		return redirect('index')
	return render(request, 'Administrador/borrarcategoría.html', {'categoría':categoría})