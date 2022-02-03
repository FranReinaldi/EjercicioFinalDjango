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
        widgets = {'user': forms.HiddenInput()}

    name = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Descripcion',widget=forms.TextInput(attrs={'class': 'form-control'}))
    expire_date = forms.DateTimeField(label='Fecha de vencimiento',widget=forms.NumberInput(attrs={'type': 'date'}))
    user = forms.ModelChoiceField(widget=forms.Select(attrs={
        'class':"form-control",}),
                              required=True,
                              error_messages={
                              'required':'Seleccione usuario'
                              },
                              queryset=User.objects.all()
	)
	 
	
	

class EditForm(ModelForm):
	
	#formulario de edicion de tareas
	
    class Meta:
        model = Tarea
        fields = ['name', 'description','comments','status']
    name = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Descripcion',widget=forms.TextInput(attrs={'class': 'form-control'}))
    comments = forms.CharField(label='Comentarios',widget=forms.TextInput(attrs={'class': 'form-control'}))
  
    

class NewUserForm(UserCreationForm):
	
	#formulario de registro de nuevos usuarios
	
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
#password1 y password2 hacen referencia a contraseña y confirmar contraseña respectivamente
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user