from django import forms
from .models import Producto

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
