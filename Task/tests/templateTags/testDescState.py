from django.test import TestCase
import Task.templatetags.descState as d

class testDateTag(TestCase):

    def testCase0(self):
        n = 0
        assert d.descState(n) == 'Por hacer'

    def testCase1(self):
        n = 1
        assert d.descState(n) == 'En proceso' 
            
    def testCase2(self):
        n = 2
        assert d.descState(n) == 'Cancelada' 
            
    def testCase3(self):
        n = 3
        assert d.descState(n) == 'Finalizada' 
        