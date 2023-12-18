from django.test import TestCase
import Task.templatetags.formatTitle as formatTitle

class testDateTag(TestCase):

    def testCaseLess18(self):
        n = 'menos de 18'
        assert formatTitle(n) == 'menos de 18'

    def testCaseMore15(self):
        n = 'muchos mas caracteres que 18'
        assert formatTitle(n) == 'muchos mas cara...'    
        