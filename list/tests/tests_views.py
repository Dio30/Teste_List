from django.test import TestCase
from django.urls import reverse

class CarrosListViewTest(TestCase):
    def test_status_code_200(self):
        resposta = self.client.get(reverse('lista'))
        self.assertEquals(resposta.status_code, 200)
    def test_template_usado(self):
        resposta = self.client.get(reverse('lista'))
        self.assertTemplateUsed(resposta, 'to_do_list/to_do_list.html')

class CarrosNovoViewsTest(TestCase):
    def test_status_code_200(self):
        resposta = self.client.get(reverse('novo_carro'))
        self.assertEquals(resposta.status_code, 200)  
    def test_template_usado(self):
        resposta = self.client.get(reverse('novo_carro'))
        self.assertTemplateUsed(resposta, 'to_do_list/to_do_list_form.html')