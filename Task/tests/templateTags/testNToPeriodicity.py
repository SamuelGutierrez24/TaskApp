from django.test import TestCase
import Task.templatetags.nToPeriodicity as nt

class testNToPeriodicity(TestCase):

    def testCase0(self):
        n = 0
        assert nt.nToPeriodicity(n) == 'No periodico'

    def testCase1(self):
        n = 1
        assert nt.nToPeriodicity(n) == 'Diario'  
          
    def testCase2(self):
        n = 2
        assert nt.nToPeriodicity(n) == 'Semanal'  
          
    def testCase3(self):
        n = 3
        assert nt.nToPeriodicity(n) == 'Mensual'   
         
    def testCase4(self):
        n = 4
        assert nt.nToPeriodicity(n) == 'Anual'            
        