from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarrosList.as_view(), name='lista'),
    path('novo_carro/', views.CarrosNovo.as_view(), name='novo_carro'),
    path('lista_donos/', views.ProprietarioList.as_view(), name='proprietarios_list'),
    path('novo_proprietario/', views.ProprietarioNovo.as_view(), name='novo_proprietario'),
]