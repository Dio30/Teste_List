from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarrosList.as_view(), name='lista'),
    path('novo_carro/', views.CarrosNovo.as_view(), name='novo_carro'),
]