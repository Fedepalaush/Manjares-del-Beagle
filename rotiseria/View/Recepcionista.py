from django.views.generic import CreateView, ListView
from rotiseria.models import Bloque
from rotiseria.forms import BloqueForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class CrearBloque(CreateView):
    login_required(login_url='registro')
    model = Bloque
    form_class = BloqueForm
    template_name = 'Recepcionista/crearBloque.html'
    success_url = reverse_lazy('index')

@method_decorator(login_required, name='dispatch')
class ListarBloque(ListView):
    login_required(login_url='registro')
    model = Bloque
    template_name = "Recepcionista/listarBloque.html"
    form_class = BloqueForm

    def get(self, request, *args, **kwargs):
        bloques = Bloque.objects.all()
        context_dict = {'bloques': bloques}
        return render(request, self.template_name, context=context_dict)

@login_required(redirect_field_name='login')
def BorrarBloque(request, id):
	bloque = Bloque.objects.get(id=id)
	if request.method == 'POST':
		bloque.delete()
		return redirect('index')
	return render(request, 'Recepcionista/borrarBloque.html', {'bloque':bloque})
