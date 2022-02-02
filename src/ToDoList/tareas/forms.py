from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tarea



class CreationForm(ModelForm):
	
	#formulario de Creacion de nuevas tareas
	
    class Meta:
        model = Tarea
        fields = ['name', 'description', 'expire_date','user']
	
	

class EditForm(ModelForm):
	
	#formulario de edicion de tareas
	
    class Meta:
        model = Tarea
        fields = ['name', 'description','comments','status']

class NewUserForm(UserCreationForm):
	
	#formulario de registro de nuevos usuarios
	
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user