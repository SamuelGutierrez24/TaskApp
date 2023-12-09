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
    
    category = nameModelChoiceField( label = "Categoria", required = True,
        queryset=models.Category.objects.order_by('name'),
        widget=forms.Select(attrs={'class': 'select2'}),    
    )
        
    color = forms.CharField(widget=forms.TextInput(attrs={'type':'color'}))
    
    taskState = forms.ChoiceField(label="Estado", choices=models.Task.state.choices)
    
    class Meta:
        
        model = models.Task
        fields = [
            'category',
            'color',
            'taskState'
        ]


class categoryCreationForm(ModelForm):
    
    class Meta:
        model = models.Category
        fields = [
            'name',
            'description'
        ]
    