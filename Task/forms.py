from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.widgets import NumberInput
from django.forms import Form
from django import forms
import Task.models as models
from django.db import models as djangoModels
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.db.models import Value
from django.db.models import CharField
from django.db.models import F
from django.db.models.functions import Concat
from django.utils.translation import gettext_lazy as _

class nameModelChoiceField(forms.ModelChoiceField):
        def label_from_instance(self, obj: Model) -> str:
            return obj.name
        
        
        

class taskCreationForm(ModelForm):
    
    
    taskName = forms.CharField(label = 'Nombre')    
    category = nameModelChoiceField( label = "Categoria",required=True,
        queryset=models.Category.objects.order_by('name'),
        widget=forms.Select(attrs={'class': 'select2'}),    
    ) 
    color = forms.CharField(widget=forms.TextInput(attrs={'type':'color'}))
    taskState = forms.ChoiceField(label='Estado', choices=models.Task.state.choices)
    periodicity = forms.ChoiceField(label='Periodicidad', choices=models.Task.period.choices)
    dueDate = forms.DateField(label='Fecha de vencimiento', widget=forms.TextInput(attrs={'type':'date'}))
    dueTime = forms.TimeField(label='Hora de vencimiento', widget=forms.TextInput(attrs={'type':'time'}))

    class Meta:
        
        model = models.Task
        fields = [
            'taskName',
            'category',
            'color',
            'taskState',
            'periodicity',
            'dueDate',
            'dueTime',
            'user'
        ]
        widgets = {
            'user': forms.HiddenInput(),  # Este campo se llenará automáticamente con el usuario logueado
        }


class categoryCreationForm(ModelForm):
    name = forms.CharField(label="Nombre")
    description = forms.CharField(label="Descripcion", widget=forms.Textarea())
    class Meta:
        model = models.Category
        fields = [
            'name',
            'description',
            'user'
        ]
        widgets = {
            'user': forms.HiddenInput(),  # Este campo se llenará automáticamente con el usuario logueado
        }


class extraDataForm(forms.Form):
    name = forms.CharField(label="Nombre", required=False)
    description = forms.CharField(label="Descripcion", widget=forms.Textarea(), required=False)
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

class basicFilters(forms.Form):
    category = forms.ModelChoiceField(label = "Categoria",
        queryset=models.Category.objects.all(),to_field_name='name',
        widget=forms.Select(attrs={'class': 'select2', 'onchange':'catSearch()'}),    
    ) 
    
    class state(djangoModels.IntegerChoices):
        EMPTY = 5, _('------')
        TODO = 0, _('Por hacer')
        IN_PROG = 1, _('En proceso')
        CANCELED = 2, _('Cancelada')
        FINISHED = 3, _('Finalizada')
    
    taskState = forms.ChoiceField(label='Estado', choices=state.choices, 
                                  widget=forms.Select(attrs={'class': 'select2', 'onchange':'stateSearch()'}))