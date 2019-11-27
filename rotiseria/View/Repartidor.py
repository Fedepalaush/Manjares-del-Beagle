from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from rotiseria.models import Pedido, Mapa
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

@login_required(redirect_field_name='login')
@permission_required('rotiseria.es_repart')
def mapa(request):
    return render (request,'Repartidor/index.html')


@method_decorator(login_required, name='dispatch')
class ListarDatosMapa (PermissionRequiredMixin,ListView):
    login_required(login_url='registro')
    permission_required = 'rotiseria.es_repart'
    model = Mapa
    template_name = "Repartidor/index.html"

    def get(self, request, *args, **kwargs):
<<<<<<< HEAD
        mapas = Mapa.objects.all()
        context_dict = {'mapas': mapas}
=======
        #mapas = Mapa.objects.all()
        pedidos = Pedido.objects.filter(bloque = 1)
        context_dict = {'pedidos': pedidos}
>>>>>>> c186011b03e9473ce49e2e6847def7a422647c57
        return render(request, self.template_name, context=context_dict)

    def obtenerDatosPedido(self,request):
        mapas = Mapa.objects.all()
        pedido = Pedido.objects.all()

        context_dict = {'mapas': mapas, 'pedido': pedido}
        return render(request, self.template_name, context=context_dict)


