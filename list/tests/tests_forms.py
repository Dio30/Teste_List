from django.test import TestCase
from proprietarios.models import Proprietarios
from ..forms import CarrosForm

class CarrosFormTest(TestCase):
    
    def test_carros_form_valido(self):
        user= Proprietarios.objects.create(nome='dione')
        form = CarrosForm(data={
            "nome_do_carro": "gol", 
            "cor": "yellow", 
            "modelos": "hatch",
            "proprietarios": user,
            })
        self.assertTrue(form.is_valid())
    
    def test_carros_form_invalido(self): #para saber se acontece erro no form com os dados vazios, se estiver retorna True
        form = CarrosForm(data={})
        self.assertFalse(form.is_valid())