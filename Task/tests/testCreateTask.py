from django.test import TestCase
import Task.views.createTasks as createTasks
import Task.models as models
from django.contrib.auth.hashers import make_password
from django.urls import reverse

class testCreateTask(TestCase):

    def setup(self):
        user = models.User(password = make_password('password'), username='usuario', first_name='usua', last_name='rio', email='usuario@gmail.com')
        user.save()
        
        
    def testAccess(self):
        login = self.client.login(username='usuario', password='usuario')
        response = self.client.get(reverse('createTasks'))
        
        self.assertEquals(response.status_code,200)
    
    def testCreation(self):
        login = self.client.login(username='usuario', password='usuario')
        response = self.client.post(reverse('createTask'), kwargs={''})