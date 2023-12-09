from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from datetime import datetime
from colorfield.fields import ColorField
from colorfield.fields import ColorWidget

class Category(models.Model):
    idCat = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()


class Task(models.Model):
    idTask = models.IntegerField(primary_key=True, auto_created=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = ColorField(default='#FFFFFF')
    
    class state(models.IntegerChoices):
        TODO = 0, _('Por hacer')
        IN_PROG = 1, _('En proceso')
        CANCELED = 2, _('Cancelada')
        FINISHED = 3, _('Finalizada')
    
    taskState = models.IntegerField(default=state.TODO, choices=state.choices)
    

class ExtraData(models.Model):
    idExtra = models.IntegerField(primary_key=True, auto_created=True)
    nameExtra = models.CharField(max_length=100, blank=False)
    contentExtra = models.TextField()
    
    
