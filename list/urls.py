from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarrosList.as_view(), name='lista'),
    path('novo_carro/', views.CarrosNovo.as_view(), name='novo_carro'),
    path('editar_carro/<int:pk>/', views.CarroUpdate.as_view(), name='editar_carro'),
    path('deletar_carro/<int:pk>/', views.CarroDelete.as_view(), name='deletar_carro'),
    path('lista_donos', views.ProprietarioList.as_view(), name='proprietarios_list'),
    path('novo_proprietario/', views.ProprietarioNovo.as_view(), name='novo_proprietario'),
    path('editar_proprietario/<int:pk>/', views.ProprietarioUpdate.as_view(), name='editar_proprietario'),
]