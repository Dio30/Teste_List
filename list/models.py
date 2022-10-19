from django.db import models

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

class Proprietarios(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    possivel_venda = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Proprietario'
        verbose_name_plural = 'Proprietarios'
        ordering = ['id',]
    
    def __str__(self):
        return self.nome

class Carros(models.Model):
    nome_do_carro = models.CharField(max_length=200, unique=True, verbose_name='Carro')
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