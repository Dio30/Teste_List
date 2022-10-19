from django.test import TestCase
from ..models import Carros, Proprietarios

class CarrosTest(TestCase):
    def setUp(self):
        user= Proprietarios.objects.create(nome='dione')
        Carros.objects.create(
            nome_do_carro='gol',
            cor='yellow',
            modelos='hatch',
            proprietarios= user
        )
    
    def test_return_str(self):
        carro = Carros.objects.get(nome_do_carro='gol')
        self.assertEqual(carro.__str__(), 'gol')

class ProprietariosTest(TestCase):
    def setUp(self):
        Proprietarios.objects.create(nome='dione')
    
    def test_return_str(self):
        proprietarios = Proprietarios.objects.get(nome='dione')
        self.assertEqual(proprietarios.__str__(), 'dione')