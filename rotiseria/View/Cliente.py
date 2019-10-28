from django.views.generic import CreateView, ListView
from django.shortcuts import render, redirect
from rotiseria.models import Cliente, Pedido, Producto, Categoría
from rotiseria.forms import ClienteForm, PedidoForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

def quienesSomos(request):
    request.session.flush()
    request.session['alimentos'] = {}
    request.session['items'] = 0
    return render(request, 'Cliente/quienesSomos.html')

def indexCliente(request):
    
    categorias = Categoría.objects.all()
    productos = Producto.objects.all()
    #Numero de visitas contadas en esta variable de sesion
    num_visitas = request.session.get('num_visitas', 0)
    request.session['num_visitas'] = num_visitas+1
    contexto = {'productos': productos, 'categorias': categorias, 'num_visitas': num_visitas}
    return render(request, 'Cliente/index.html', contexto)

class CrearCliente(CreateView):
    login_required(login_url='registro')
    model = Cliente
    form_class = ClienteForm
    template_name = 'Cliente/crearCliente.html'
    success_url = reverse_lazy('index')

@method_decorator(login_required, name='dispatch')
class ListarCliente(ListView):
    login_required(login_url='registro')
    model = Cliente
    template_name = "Cliente/listarCliente.html"
    form_class = ClienteForm

    def get(self, request, *args, **kwargs):
        clientes = Cliente.objects.all()
        context_dict = {'clientes': clientes}
        return render(request, self.template_name, context=context_dict)

@login_required(redirect_field_name='login')
def BorrarCliente(request, dni):
	cliente = Cliente.objects.get(dni=dni)
	if request.method == 'POST':
		cliente.delete()
		return redirect('index')
	return render(request, 'Cliente/borrarCliente.html', {'cliente':cliente})

class CrearPedido(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'Cliente/crearPedido.html'
    success_url = reverse_lazy('index')

class ListarPedido(ListView):
    model = Pedido
    template_name = "Cliente/listarPedidos.html"
    form_class = PedidoForm

    def get(self, request, *args, **kwargs):
        pedidos = Pedido.objects.all()
        context_dict = {'pedidos': pedidos}
        return render(request, self.template_name, context=context_dict)
