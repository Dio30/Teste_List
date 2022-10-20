from django.db import models

class Proprietarios(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    possivel_venda = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Proprietário'
        verbose_name_plural = 'Proprietários'
        ordering = ['id',]
    
    def __str__(self):
        return self.nome