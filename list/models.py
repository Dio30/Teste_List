from django.db import models
from proprietarios.models import Proprietarios

colors = (
    ("yellow", "yellow"),
    ("blue", "blue"),
    ("gray", "gray"),
)

model = (
    ("hatch", "hatch"),
    ("sedan", "sedan"),
    ("convertible", "convertible"),
)

class Carros(models.Model):
    nome_do_carro = models.CharField(max_length=200, verbose_name='Carro')
    cor = models.CharField(max_length=200, choices=colors)
    modelos = models.CharField(max_length=200, choices=model)
    proprietarios = models.ForeignKey(Proprietarios, on_delete=models.CASCADE, related_name="proprietarios", 
                                      related_query_name= 'proprietarios',verbose_name='Proprietário')
    
    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
        ordering = ['nome_do_carro',]
        
    def __str__(self):
        return self.nome_do_carro