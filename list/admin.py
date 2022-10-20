from django.contrib import admin
from .models import Carros
from .forms import CarrosForm

class CarrosAdmin(admin.ModelAdmin):
    list_display = ["nome_do_carro", "cor", "modelos", "proprietarios"]
    form = CarrosForm

admin.site.register(Carros, CarrosAdmin)