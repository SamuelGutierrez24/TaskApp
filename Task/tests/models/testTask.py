from django.test import TestCase
import Task.views.createTasks as createTasks
import Task.models as models
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from Task.forms import taskCreationForm

class testTask(TestCase):

    def testCreateTask(self):
        user = models.User(password =make_password('password'), username='usuario', first_name='usua', last_name='rio', email='usuario@gmail.com')
        user.save()
        mod = models.Task(taskName='task',taskDescription='desc',category=models.Category.objects.get(id=1),color='#000000',user=user,taskState=0,periodicity=0,dueDate='2023-12-12',dueTime='12:12').save()
        
        self.assertEquals(mod.taskName, 'task')
        self.assertEquals(mod.taskDescription, 'desc')
        self.assertEquals(mod.category, models.Category.objects.get(id=1))
        self.assertEquals(mod.color, '#000000')
        self.assertEquals(mod.user, user)
        self.assertEquals(mod.taskState, 0)
        self.assertEquals(mod.periodicity, 0)
        self.assertEquals(mod.dueDate, '2023-12-12')
        self.assertEquals(mod.dueTime, '12:12')