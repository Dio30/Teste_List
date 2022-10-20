from django.test import TestCase
from django.urls import reverse

class ProprietariosListViewTest(TestCase):
    def test_status_code_200(self):
        resposta = self.client.get(reverse('proprietarios_list'))
        self.assertEquals(resposta.status_code, 200)
    def test_template_usado(self):
        resposta = self.client.get(reverse('proprietarios_list'))
        self.assertTemplateUsed(resposta, 'proprietarios/proprietarios_list.html')
        
class ProprietariosNovoViewsTest(TestCase):
    def test_status_code_200(self):
        resposta = self.client.get(reverse('novo_proprietario'))
        self.assertEquals(resposta.status_code, 200)
    def test_template_usado(self):
        resposta = self.client.get(reverse('novo_proprietario'))
        self.assertTemplateUsed(resposta, 'proprietarios/proprietarios_form.html')