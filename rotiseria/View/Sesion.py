from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as loggin

from django.views.generic import FormView, CreateView
from rotiseria.forms import RegistroForm, UserForm

from django.contrib.auth.models import User
from rotiseria.models import Rol, Usuario
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group



class SignIn(FormView):
    template_name = 'Sesion/login.html'
    form_class = UserForm
    model = Usuario



    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, template_name=self.template_name, context={form: form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print (form.is_valid())
        if form.is_valid():
            alias = form.cleaned_data.get('username')
            user = Usuario.objects.get(alias=alias)
            if user.rol.nombre == 'Administrador':
                return redirect('index_administrador')
            if user.rol.nombre == 'Recepcionista':
                return redirect('listar:_producto')
            elif user.rol.nombre == ('Repartidor'):
                return redirect('mapa')
            else:
                return redirect('quienesSomos')
        return render(request, template_name=self.template_name, context={form:form})

@user_passes_test(lambda u: u.is_superuser)
def register(request):
    if request.method == "POST":
        u_form = UserForm(request.POST)
        if u_form.is_valid():
            user = u_form.save()
            rol_obtenido = str(u_form.cleaned_data['rol'])
            objeto_rol = Rol.objects.get(nombre=rol_obtenido)
            mi_usuario = Usuario.objects.create(user=user, rol = objeto_rol)
            mi_usuario.save()
            return redirect('login')
    else:
        u_form = UserForm(request.POST)
    return render(request, 'Sesion/registro.html', {'u_form': u_form})


def login(request):
    totalUsuarios= Usuario.objects.all()
    usersup= User.objects.all()
    for i in usersup:
        if i.is_superuser:
            superuser=i.username
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            users = User.objects.filter(username=username)
            user = users[0]
            usuariosuper= User.objects.filter (username=superuser)
            supus= usuariosuper[0]

            user = form.get_user()
            loggin(request, user)

            if (supus.username== username):
                return redirect('registro')
            usuarios=Usuario.objects.filter(user__id=user.id)
            if usuarios[0].rol.nombre == 'Recepcionista':
                return redirect('listar_producto')
            if usuarios[0].rol.nombre == ('Administrador'):
                return redirect('index_administrador')
            if usuarios[0].rol.nombre == 'Repartidor':
                return redirect('listar_datos_mapa')



    else:
        form = AuthenticationForm()
    return render (request, "Sesion/login.html", {'form':form})