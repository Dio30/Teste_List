from django import forms
from .models import Carros
from django.core.exceptions import ValidationError

class CarrosForm(forms.ModelForm):
    
    class Meta:
        model = Carros
        fields = ["nome_do_carro", "cor", "modelos", "proprietarios"]
        
    def clean_proprietarios(self):
        n = self.cleaned_data['proprietarios']
        nome = Carros.objects.filter(proprietarios=n)
        if nome.count() >= 3:
            raise ValidationError(f'O proprietário {n} só pode ter 3 carros.')
        return n