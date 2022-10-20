from django.contrib import admin
from .models import Proprietarios

class ProprietariosAdmin(admin.ModelAdmin):
    list_display = ["nome", "possivel_venda",]

admin.site.register(Proprietarios, ProprietariosAdmin)
