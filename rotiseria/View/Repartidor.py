from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from rotiseria.models import Pedido, Mapa, Bloque
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

@login_required(redirect_field_name='login')
@permission_required('rotiseria.es_repart')
def mapa(request):
    return render (request,'Repartidor/index.html')



class ListarDatosMapa (ListView):
    model = Mapa
    template_name = "Repartidor/index.html"

    def get(self, request, *args, **kwargs):
        if not(request.user.has_perm('rotiseria.es_repart')):
                return redirect(reverse_lazy('login'))
        bloques = Bloque.objects.all()
        #bloques empieza del ID 0 (cero)
        id = len(bloques) - 1
        ultimo_Bloque = bloques[id]

        pedidos_bloque = Pedido.objects.filter(bloque = ultimo_Bloque.id)
        context_dict = {'pedidos_bloque': pedidos_bloque}
        return render(request, self.template_name, context=context_dict)

    def obtenerDatosPedido(self,request):
        mapas = Mapa.objects.all()
        pedidos = Pedido.objects.all()

        context_dict = {'mapas': mapas, 'pedidos': pedidos}
        return render(request, self.template_name, context=context_dict)


