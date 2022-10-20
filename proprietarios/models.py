from django.db import models

class Proprietarios(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    possivel_venda = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Proprietario'
        verbose_name_plural = 'Proprietarios'
        ordering = ['id',]
    
    def __str__(self):
        return self.nome