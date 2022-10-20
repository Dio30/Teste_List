from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import Carros
from .forms import CarrosForm

class CarrosList(ListView):
    model = Carros
    queryset = Carros.objects.order_by('proprietarios_id')
    template_name = 'to_do_list/to_do_list.html'
    context_object_name = 'carros_list'
    paginate_by = 5
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['carros'] = Carros.objects.count()
        return context

class CarrosNovo(SuccessMessageMixin, CreateView):
    form_class= CarrosForm
    success_url = reverse_lazy('lista')
    template_name = 'to_do_list/to_do_list_form.html'
    success_message = 'Carro adicionado com sucesso!'
    
    def form_valid(self, form):
        url = super().form_valid(form)
        return url