from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from rotiseria.models import Mapa

def mapa(request):
    return render (request,'Repartidor/index.html')

class ListarDatosMapa (ListView):
    model = Mapa
    template_name = "Repartidor/index.html"

    def get(self, request, *args, **kwargs):
        mapas = Mapa.objects.all()
        print(mapas)
        context_dict = {'mapas': mapas}
        return render(request, self.template_name, context=context_dict)