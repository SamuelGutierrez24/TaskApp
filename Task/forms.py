from django.db.models.base import Model
from django.forms import ModelForm
from django import forms
import Task.models as models
from django.db import models as djangoModels
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User  # Importa el modelo de usuario de Django


class nameModelChoiceField(forms.ModelChoiceField):
        def label_from_instance(self, obj: Model) -> str:
            return obj.name
        
        
        

class taskCreationForm(ModelForm):
    
    
    taskName = forms.CharField(label = 'Nombre')    
    taskDescription = forms.CharField(label = 'Descripcion', widget=forms.Textarea, required=False)
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
            'taskDescription',
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
    
    class state(djangoModels.TextChoices):
        EMPTY = '', _('------')
        TODO = 'Por hacer', _('Por hacer')
        IN_PROG = 'En proceso', _('En proceso')
        CANCELED = 'Cancelada', _('Cancelada')
        FINISHED = 'Finalizada', _('Finalizada')
    
    taskState = forms.ChoiceField(label='Estado', choices=state.choices,
                                  widget=forms.Select(attrs={'class': 'select2', 'onchange':'stateSearch()'}))
    
    startDate = forms.DateField(label = "Desde", widget = forms.DateInput(attrs={'onchange':'startDate()', 'type':'date'}))
    endDate = forms.DateField(label = "Hasta", widget = forms.DateInput(attrs={'onchange':'endDate()', 'type':'date'}))
    