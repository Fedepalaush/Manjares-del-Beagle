from django.views.generic import CreateView, ListView
from rotiseria.models import Bloque
from rotiseria.forms import BloqueForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

class CrearBloque(CreateView):
    model = Bloque
    form_class = BloqueForm
    template_name = 'Recepcionista/crearBloque.html'
    success_url = reverse_lazy('index')


class ListarBloque(ListView):
    model = Bloque
    template_name = "Recepcionista/listarBloque.html"
    form_class = BloqueForm

    def get(self, request, *args, **kwargs):
        bloques = Bloque.objects.all()
        context_dict = {'bloques': bloques}
        return render(request, self.template_name, context=context_dict)

def BorrarBloque(request, id):
	bloque = Bloque.objects.get(id=id)
	if request.method == 'POST':
		bloque.delete()
		return redirect('index')
	return render(request, 'Recepcionista/borrarBloque.html', {'bloque':bloque})
