from django.test import TestCase
import Task.templatetags.descState as descState

class testDateTag(TestCase):

    def testCase0(self):
        n = 0
        assert descState(n) == '¨Por hacer'

    def testCase1(self):
        n = 1
        assert descState(n) == 'En proceso' 
            
    def testCase2(self):
        n = 2
        assert descState(n) == 'Cancelada' 
            
    def testCase3(self):
        n = 3
        assert descState(n) == 'Finalizada' 
        