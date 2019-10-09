from django import forms
from .models import Producto, Categoría, Cliente, Bloque

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
			'dni',
			'nombre',
			'telefono',
			'direccion',
		]
		labels = {
			'dni': 'DNI',
			'nombre': 'Nombre',
			'telefono': 'Telefono',
			'direccion': 'Direccion'}


