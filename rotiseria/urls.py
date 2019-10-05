from django.urls import path
from .View.principal import index
from rotiseria.View.Administrador import ProductoCreate
urlpatterns = [

path('', index, name='home'),
path('crearproducto',ProductoCreate.as_view(), name = 'crear_producto'),
]