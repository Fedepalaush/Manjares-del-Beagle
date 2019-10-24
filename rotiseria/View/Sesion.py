from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView
from rotiseria.forms import RegistroForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from rotiseria.models import Rol
from django.shortcuts import render


class SignIn(FormView):
    template_name = 'Sesion/login.html'
    success_url = reverse_lazy('mapa')
    form_class = AuthenticationForm

    def dispatch(self, request, *args, **kwargs):
        return super(SignIn, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(SignIn, self).form_valid(form)


class RegistroUsuario(CreateView):
    model = User
    template_name = "Sesion/registro.html"
    form_class = RegistroForm
    success_url = reverse_lazy('mapa')

    def get(self, request, *args, **kwargs):
        roles = Rol.objects.all()
        context_dict = {'roles': roles}
        return render(request, self.template_name, context=context_dict)