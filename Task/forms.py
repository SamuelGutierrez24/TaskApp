from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.widgets import NumberInput
from django.forms import Form
from django import forms
import Task.models as models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.db.models import Value
from django.db.models import CharField
from django.db.models import F
from django.db.models.functions import Concat


class taskCreationForm(ModelForm):
    
    class nameModelChoiceField(forms.ModelChoiceField):
        def label_from_instance(self, obj: Model) -> str:
            return obj.name
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
            'dueTime'
        ]


class categoryCreationForm(ModelForm):
    name = forms.CharField(label="Nombre")
    description = forms.CharField(label="Descripcion", widget=forms.Textarea())
    class Meta:
        model = models.Category
        fields = [
            'name',
            'description'
        ]


class extraDataForm(forms.Form):
    name = forms.CharField(label="Nombre", required=False)
    description = forms.CharField(label="Descripcion", widget=forms.Textarea(), required=False)
    