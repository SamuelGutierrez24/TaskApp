from django.test import TestCase
import Task.views.createTasks as createTasks
import Task.models as models
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from Task.forms import taskCreationForm

class testTask(TestCase):

    def testCreateTask(self):

        mod = models.Category(name='cat',description='desc')
        self.assertEquals(mod.name, 'cat')
        self.assertEquals(mod.description, 'desc')
        