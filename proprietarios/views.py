from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import Proprietarios

class ProprietarioList(ListView):
    model = Proprietarios
    queryset = Proprietarios.objects.order_by('nome')
    template_name = 'proprietarios/proprietarios_list.html'
    context_object_name = 'proprietarios_list'
    ordering = 'id'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['proprietarios'] = Proprietarios.objects.count()
        return context
    
class ProprietarioNovo(SuccessMessageMixin, CreateView):
    model = Proprietarios
    fields = ["nome", "possivel_venda"]
    success_url = reverse_lazy('proprietarios_list')
    template_name = 'proprietarios/proprietarios_form.html'
    success_message = 'Proprietário adicionado com sucesso!'
    
    def form_valid(self, form):
        url = super().form_valid(form)
        return url