from django import forms
from .models import Producto, Categoría, Cliente, Bloque, Pedido
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProductoForm(forms.ModelForm):

	class Meta:
		model = Producto

		fields = [
			'nombre',
			'descripcion',
            'foto',
            'precioActual',
			'categoria',
			'ganancia',
		]
		labels = {
			'nombre': 'Nombre',
			'descripcion': 'Descripcion',
            'foto': 'Foto',
            'precioActual': 'Precio Actual',
			'categoria':'Categoria',
		    'Ganancia': 'Ganancia',
		}

class CategoriaForm (forms.ModelForm):
	class Meta:
		model = Categoría

		fields = [
			'nombre',

		]
		labels = {
			'nombre': 'Nombre'}


class BloqueForm(forms.ModelForm):
	class Meta:
		model = Bloque

		fields = [
			'id',
			'fecha',
			'usuario',
		]
		labels = {
			'id': 'ID',
			'fecha': 'Fecha',
			'usuario': 'Usuario'}



class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente

		fields = [
			'nombre',
			'telefono',

		]
		labels = {
			'nombre': 'Nombre',
			'telefono': 'Telefono',}


class PedidoForm(forms.ModelForm):
	class Meta:
		model = Pedido
		fields = [
			'fecha',
			'total',
			'productos',
			'bloque',
			'cliente',
			'estadoPedido',
		]
		labels = {
			'fecha': 'Fecha',
			'total': 'Total',
			'productos':'Productos',
			'bloque': 'Bloque',
			'cliente': 'Cliente',
			'estadoPedido': 'EstadoPedido'}


class RegistroForm(UserCreationForm):

	rol = forms.CharField(required=True)
	class Meta:
			model = User
			fields = [
				'username',
				'first_name',
				'last_name',
				'password1',
				'password2',
				'rol'
			]



	def save (self, commit=True):
		user = super(RegistroForm,self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.rol = self.cleaned_data['rol']

		if commit:
			user.save()

		return user


class PedidoAlimentoForm(forms.Form):

    alimento = forms.IntegerField()
    cantidad = forms.IntegerField()

class ProductoIDForm(forms.Form):

    alimento = forms.IntegerField()

class DatosClienteForm(forms.Form):

	nombreApellido = forms.CharField()
	celular = forms.IntegerField()
	descripcion = forms.CharField()
	direccion = forms.CharField()