from django.test import TestCase
import Task.templatetags.nToPeriodicity as nToPeriodicity

class testNToPeriodicity(TestCase):

    def testCase0(self):
        n = 0
        assert nToPeriodicity(n) == 'No periodico'

    def testCase1(self):
        n = 1
        assert nToPeriodicity(n) == 'Diario'  
          
    def testCase2(self):
        n = 2
        assert nToPeriodicity(n) == 'Semanal'  
          
    def testCase3(self):
        n = 3
        assert nToPeriodicity(n) == 'Mensual'   
         
    def testCase4(self):
        n = 4
        assert nToPeriodicity(n) == 'Anual'            
        