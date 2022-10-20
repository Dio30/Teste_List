from django.urls import path
from . import views

urlpatterns = [
    path('lista_proprietarios/', views.ProprietarioList.as_view(), name='proprietarios_list'),
    path('novo_proprietario/', views.ProprietarioNovo.as_view(), name='novo_proprietario'),
    ]