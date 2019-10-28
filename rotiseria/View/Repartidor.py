from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from rotiseria.models import Mapa

from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')
def mapa(request):
    return render (request,'Repartidor/index.html')

class ListarDatosMapa (ListView):
    model = Mapa
    template_name = "Repartidor/index.html"

    def get(self, request, *args, **kwargs):
        mapas = Mapa.objects.all()
        context_dict = {'mapas': mapas}
        return render(request, self.template_name, context=context_dict)