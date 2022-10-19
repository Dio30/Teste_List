from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import Carros, Proprietarios
from .forms import CarrosForm

class CarrosList(ListView):
    model = Carros
    queryset = Carros.objects.order_by('proprietarios_id')
    template_name = 'to_do_list/to_do_list.html'
    paginate_by = 4

class CarrosNovo(SuccessMessageMixin, CreateView):
    form_class= CarrosForm
    success_url = reverse_lazy('lista')
    template_name = 'to_do_list/to_do_list_form.html'
    success_message = 'Carro adicionado com sucesso!'
    
    def form_valid(self, form):
        url = super().form_valid(form)
        return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastrar"
        return context

class CarroUpdate(SuccessMessageMixin, UpdateView):
    form_class= CarrosForm
    success_url = reverse_lazy('lista')
    template_name = 'to_do_list/to_do_list_form.html'
    success_message = 'Carro editado com sucesso!'
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Carros, pk=self.kwargs['pk'])
        return self.object
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar"
        return context

class CarroDelete(SuccessMessageMixin, DeleteView):
    queryset = Carros.objects.all()
    success_url = reverse_lazy('lista')
    success_message = 'Carro deletado com sucesso!'
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Carros, pk=self.kwargs['pk'])
        return self.object

class ProprietarioList(ListView):
    model = Proprietarios
    queryset = Proprietarios.objects.order_by('nome')
    template_name = 'proprietarios/proprietarios_list.html'
    
class ProprietarioNovo(SuccessMessageMixin, CreateView):
    model = Proprietarios
    fields = ["nome", "possivel_venda"]
    success_url = reverse_lazy('proprietarios_list')
    template_name = 'proprietarios/proprietarios_form.html'
    success_message = 'Proprietário adicionado com sucesso!'
    
    def form_valid(self, form):
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastrar Proprietário"
        return context
    
class ProprietarioUpdate(SuccessMessageMixin, UpdateView):
    model = Proprietarios
    fields = ["nome", "possivel_venda"]
    success_url = reverse_lazy('proprietarios_list')
    template_name = 'proprietarios/proprietarios_form.html'
    success_message = 'Proprietário editado com sucesso!'
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Proprietarios, pk=self.kwargs['pk'])
        return self.object
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar"
        return context