from django.test import TestCase
import Task.templatetags.dateTag as d

class testDateTag(TestCase):

    def testCase0(self):
        n = 0
        assert d.dateTag(n) == 'Fecha de vencimiento'

    def testCase1(self):
            n = 1
            assert d.dateTag(n) == 'Fecha Inicial'    
        