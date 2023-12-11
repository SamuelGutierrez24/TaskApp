from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Importa el modelo de usuario de Django

class CustomUserCreationForm(UserCreationForm):
    # Puedes agregar campos adicionales aquí según tus necesidades
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True, help_text='Requerido. Ingrese una dirección de correo electrónico válida.')
    user_name = forms.CharField(max_length=50,required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmar contraseña')


    class Meta:
        model = User  # Usa el modelo de usuario importado
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
