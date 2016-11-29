from django import forms
from django.forms import ModelForm


class Formulario():
	class meta:
		fields = [
			'tiulo',
			'autor',
			'descripcion',
		]
		
		labels = {
			'tiulo' : 'Titulo',
			'autor' : 'Autor',
			'descripcion' : 'Descripcion',
		}

		widgets = {
			'tiulo' : forms.TextInput(attrs = {'class' : 'form-control'}),
			'autor' : forms.TextInput(attrs = {'class' : 'form-control'}),
			'descripcion' : forms.TextInput(attrs = {'class' : 'form-control'}),
		}