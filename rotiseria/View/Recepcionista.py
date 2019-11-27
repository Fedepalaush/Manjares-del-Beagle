from django.views.generic import CreateView, ListView
from rotiseria.models import Bloque, Pedido, PedidoProducto, EstadoPedido
from rotiseria.forms import BloqueForm, PedidoForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

@method_decorator(login_required, name='dispatch')
class CrearBloque(PermissionRequiredMixin,CreateView):
    login_required(login_url='registro')
    permission_required = 'rotiseria.es_recep'
    model = Bloque
    form_class = BloqueForm
    template_name = 'Recepcionista/crearBloque.html'
    success_url = reverse_lazy('index')

@method_decorator(login_required, name='dispatch')
class ListarBloque(PermissionRequiredMixin,ListView):
    login_required(login_url='registro')
    permission_required = 'rotiseria.es_recep'
    model = Bloque
    template_name = "Recepcionista/listarBloque.html"
    form_class = BloqueForm

    def get(self, request, *args, **kwargs):
        bloques = Bloque.objects.all()
        context_dict = {'bloques': bloques}
        return render(request, self.template_name, context=context_dict)

@login_required(redirect_field_name='login')
@permission_required('rotiseria.es_recep')
def BorrarBloque(request, id):
	bloque = Bloque.objects.get(id=id)
	if request.method == 'POST':
		bloque.delete()
		return redirect('index')
	return render(request, 'Recepcionista/borrarBloque.html', {'bloque':bloque})

class ListarPedido(ListView):
    model = Pedido
    template_name = "Recepcionista/listarPedidos.html"
    form_class = PedidoForm

    def get(self, request, *args, **kwargs):
        #Con esto le paso el total como unico valor sumado de todos los productos del pedido
        pedidos = Pedido.objects.all()
        pedidoProductos = PedidoProducto.objects.all()
        context_dict = {'pedidos': pedidos, 'pedidoProductos': pedidoProductos}
        return render(request, self.template_name, context=context_dict)

def pedidosConfirmados(request):
        pedidos = Pedido.objects.all()
        pedidoProductos = PedidoProducto.objects.all()
        context_dict = {'pedidos': pedidos, 'pedidoProductos': pedidoProductos}
        return render(request, 'Recepcionista/listarPedidosConfirmados.html', context=context_dict)

def confirmar_pedido(request, id):
    pedido = Pedido.objects.get(id =id)
    estadoDelPedido = EstadoPedido.objects.get(estado = 'confirmado')
    pedido.estadoPedido = estadoDelPedido
    pedido.save()
    return render(request, 'Recepcionista/listarPedidos.html')

def rechazar_pedido(request, id):
    pedido = Pedido.objects.get(id = id)
    estadoDelPedido = EstadoPedido.objects.get(estado = 'rechazado')
    pedido.estadoPedido = estadoDelPedido
    pedido.save()
    return render(request, 'Recepcionista/listarPedidos.html')

def pedidosRechazados(request):
    pedidos = Pedido.objects.all()
    pedidoProductos = PedidoProducto.objects.all()
    context_dict = {'pedidos': pedidos, 'pedidoProductos': pedidoProductos}
    return render(request, 'Recepcionista/listarPedidosRechazados.html', context=context_dict)    