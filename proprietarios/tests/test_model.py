from django.test import TestCase
from ..models import Proprietarios

class ProprietariosTest(TestCase):
    def setUp(self):
        Proprietarios.objects.create(nome='dione')
    
    def test_return_str(self):
        proprietarios = Proprietarios.objects.get(nome='dione')
        self.assertEqual(proprietarios.__str__(), 'dione')
