from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import DiscountRules, Consumer
from .models import Consumer, DiscountRules


class ConsumerListView(ListView):
    model = Consumer
    template_name = 'consumer_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Recuperar todas as regras de desconto do banco de dados
        discount_rules = DiscountRules.objects.all()
        
        # Calcular a economia para cada consumidor
        for consumer in context['object_list']:
            consumer_economy = 0
            for rule in discount_rules:
                if consumer.type == rule.consumer_type and consumer.consumption in rule.consumption_range:
                    consumer_economy += rule.discount_value
            consumer.economy = consumer_economy
        
        return context

def view1(request):
    # Create the first view here.
    pass


class ConsumerCreateView(CreateView):
    model = Consumer
    fields = ['name', 'document', 'type', 'consumption']  # Campos que serão exibidos no formulário
    success_url = reverse_lazy('consumer-list')

    def form_valid(self, form):
        document = form.cleaned_data['document']
        if validar_documento(document):
            consumer = form.save(commit=False)
            discount_rule = DiscountRules.objects.get(consumer_type=consumer.type, consumption_range=consumer.consumption)
            consumer.discount_rule = discount_rule
            consumer.save()
            return super().form_valid(form)
        else:
            form.add_error('document', 'Documento inválido. Por favor, insira um documento válido.')
            return self.form_invalid(form)

    def validar_documento(documento):
        cpf_validator = CPF()
        documento = ''.join(filter(str.isdigit, documento))
        if cpf_validator.validate(documento):
            return True
        else:
            return False


def view2():
    # Create the second view here.
    pass
