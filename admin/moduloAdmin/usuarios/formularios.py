#from django import forms
#from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):
	class meta:
		model = User
		fields = [
			
		]
		labels = {
			
		}