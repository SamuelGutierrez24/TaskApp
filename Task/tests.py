from django.test import TestCase
from Task.models import *
from django.urls import reverse
from Task.forms import *


class TaskCreationTestCase(TestCase):

    def test_task_creation(self):
        data = {
            
            'taskName':'Cita Medica',
            'category':'1',
            'taskDescription':'Ir a la cita de revisión de los ojos',
            'collr':'#FFFFFF',
            'taskState':'2',
            'periodicity':'0'
        }
        form = taskCreationForm(data=data)
        self.assertTrue(form.is_valid())

        # self.assertEqual(task.taskName, 'Cita Medica')
        # self.assertEqual(task.taskDescription, 'Ir a la cita de revisión de los ojos')

    # def test_vista_home(self):
    #     self.user = User.objects.create(username='user2', password='password2')
    #     data = {
    #         'username': 'user2',
    #         'password': 'password2'
    #     }
    #     response = self.client.post(reverse('signin'), data)

    #     self.assertRedirects(response, reverse('home'))
    #     print(response)
    #     self.assertEquals(response.status_code,200)
