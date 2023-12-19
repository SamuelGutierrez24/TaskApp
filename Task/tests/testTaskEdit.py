from django.test import TestCase
import Task.views.createTasks as createTasks
import Task.models as models
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from Task.forms import taskCreationForm

class testTaskEdit(TestCase):

    def setUp(self):
        user = models.User(password =make_password('password'), username='usuario', first_name='usua', last_name='rio', email='usuario@gmail.com')
        user.save()
        models.Task(taskName='task',taskDescription='desc',category=models.Category.objects.get(id=1),color='#000000',user=user,taskState=0,periodicity=0,dueDate='2023-12-12',dueTime='12:12').save()
        
    def testRedirect(self):
        response = self.client.get('/editTask/1/')
        self.assertEquals(response.status_code,302)
    
    def testAccess(self):
        login = self.client.login(username='usuario', password='password')
        response = self.client.get('/editTask/1/')
        
        self.assertEquals(response.status_code,200)
    
    def testInvID(self):
        login = self.client.login(username='usuario', password='password')
        response = self.client.get('/editTask/2/')
        
        self.assertEquals(response.status_code,404)
    