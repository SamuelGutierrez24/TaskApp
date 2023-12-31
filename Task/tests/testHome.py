from django.test import TestCase
import Task.views.createTasks as createTasks
import Task.models as models
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from Task.forms import taskCreationForm

class testHomer(TestCase):

    def setUp(self):
        user = models.User(password =make_password('password'), username='usuario', first_name='usua', last_name='rio', email='usuario@gmail.com')
        user.save()
        
    def testRedirect(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code,302)
    
    def testAccess(self):
        login = self.client.login(username='usuario', password='password')
        response = self.client.get(reverse('home'))
        
        self.assertEquals(response.status_code,200)