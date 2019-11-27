from django.views.generic import CreateView, ListView,UpdateView
from django.shortcuts import *
from rotiseria.models import Producto, Categoría
from rotiseria.forms import ProductoForm, CategoriaForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Permission

def index(request):
    return render(request, 'base.html')

@login_required(redirect_field_name='login')
@permission_required('rotiseria.es_admin')
def indexAdministrador(request):
    return render(request, 'Administrador/indexAdministrador.html')


@method_decorator(login_required, name='dispatch')
class CrearProducto (PermissionRequiredMixin,CreateView):
        login_required(login_url='registro')
        permission_required = 'rotiseria.es_admin'
        model = Producto
        form_class= ProductoForm
        template_name = 'Administrador/crearproducto.html'
        success_url = reverse_lazy('index_administrador')

        def get(self, request):
             categorias = Categoría.objects.all()
             return render(request, 'Administrador/crearproducto.html', {"categorias": categorias})

@method_decorator(login_required, name='dispatch')
class ListarProducto (PermissionRequiredMixin,ListView):
    login_required(login_url='registro')
    model = Producto
    permission_required =('rotiseria.es_admin')
    template_name = "Administrador/listarproducto.html"
    form_class = ProductoForm


    def get(self, request, *args, **kwargs):

        productos = Producto.objects.all()
        context_dict = {'productos': productos}
        return render(request, self.template_name, context=context_dict)


@login_required(redirect_field_name='login')
@permission_required('rotiseria.es_admin')
def BorrarProducto(request, nombrep):
        producto = Producto.objects.get(nombre=nombrep)
        if request.method == 'POST':
          producto.delete()
          return redirect('index_administrador')
        return render(request, 'Administrador/borrarproducto.html', )


@login_required(redirect_field_name='login')
@permission_required('rotiseria.es_admin')
def editarproducto (request, id_producto):
    producto= Producto.objects.get (id= id_producto)
    if request.method == 'GET':
        form= ProductoForm(instance=producto)
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect('index_administrador')
    return render (request, 'Administrador/editarproducto.html', {'form':form, 'producto':producto})

@method_decorator(login_required, name='dispatch')
class CrearCategoria(PermissionRequiredMixin,CreateView):
        login_required(login_url='registro')
        permission_required = ('rotiseria.es_admin')
        model = Categoría
        form_class = CategoriaForm
        template_name = 'Administrador/crearcategoria.html'
        success_url = reverse_lazy('index_administrador')


@method_decorator(login_required, name='dispatch')
class ListarCategorias (PermissionRequiredMixin,ListView):
    login_required(login_url='registro')
    permission_required = ('rotiseria.es_admin')
    model = Categoría
    template_name = "Administrador/listarcategorías.html"
    form_class = CategoriaForm

    def get(self, request, *args, **kwargs):
        categorías = Categoría.objects.all()
        context_dict = {'categorías': categorías}
        return render(request, self.template_name, context=context_dict)

@login_required(redirect_field_name='login')
@permission_required('rotiseria.es_admin')
def BorrarCategoría(request, nombrec):
        categoría = Categoría.objects.get(nombre=nombrec)
        if request.method == 'POST':
         categoría.delete()
         return redirect('index_administrador')
        return render(request, 'Administrador/borrarcategoría.html', {'categoría':categoría})