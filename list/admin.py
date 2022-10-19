from django.contrib import admin
from .models import Proprietarios, Carros
from .forms import CarrosForm

class ProprietariosAdmin(admin.ModelAdmin):
    list_display = ["nome", "possivel_venda",]

admin.site.register(Proprietarios, ProprietariosAdmin)

class CarrosAdmin(admin.ModelAdmin):
    list_display = ["nome_do_carro", "cor", "modelos", "proprietarios"]
    form = CarrosForm

admin.site.register(Carros, CarrosAdmin)