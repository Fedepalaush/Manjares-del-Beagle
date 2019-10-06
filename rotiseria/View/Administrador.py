from django.views.generic import CreateView, ListView
from django.shortcuts import render
from rotiseria.models import Producto
from rotiseria.forms import ProductoForm
from django.urls import reverse_lazy

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