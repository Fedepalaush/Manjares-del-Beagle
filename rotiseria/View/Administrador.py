from django.views.generic import CreateView
from rotiseria.models import Producto
from rotiseria.forms import ProductoForm
from django.urls import reverse_lazy

class CrearProducto (CreateView):
        model = Producto
        form_class= ProductoForm
        template_name = 'Administrador/crearproducto.html'
        success_url = reverse_lazy('index')