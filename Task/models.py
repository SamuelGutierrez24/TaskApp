from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from datetime import datetime
from colorfield.fields import ColorField
from colorfield.fields import ColorWidget
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    def __str__(self):
        return self.username

class Category(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    
    def __str__(self):
        return self.name


class Task(models.Model):
    def save(self,*args,**kwargs):
        super(Task, self).save(*args,**kwargs)
        return self
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    taskName = models.CharField(default='Tarea', max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(default="")
    color = ColorField(default='#FFFFFF')
    
    class state(models.IntegerChoices):
        TODO = 0, _('Por hacer')
        IN_PROG = 1, _('En proceso')
        CANCELED = 2, _('Cancelada')
        FINISHED = 3, _('Finalizada')
    
    taskState = models.IntegerField(default=state.TODO, choices=state.choices)
    
    class period(models.IntegerChoices):
        NON_PERIODIC = 0, _('No periodico')
        DAILY = 1, _('Diario')
        WEEKLY = 2, _('Semanal')
        MONTHLY = 3, _('Mensual')
        ANNUALLY = 4, _('Anual')
        
    periodicity = models.IntegerField(default=period.NON_PERIODIC, choices=period.choices)
    dueDate = models.DateField(default=datetime.today, blank=False)
    dueTime = models.TimeField(default='00:00', blank=True)
    def __str__(self):
        return self.taskName
    

class ExtraData(models.Model):
    nameExtra = models.CharField(max_length=100, blank=False)
    contentExtra = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, default=1)
        
    

    
