from django.db import models


class Consumer(models.Model):
    name = models.CharField("Nome do Consumidor", max_length=128)
    document = models.CharField("Documento(CPF/CNPJ)", max_length=14, unique=True)
    zip_code = models.CharField("CEP", max_length=8, null=True, blank=True)
    city = models.CharField("Cidade", max_length=128)
    state = models.CharField("Estado", max_length=128)
    consumption = models.IntegerField("Consumo(kWh)", blank=True, null=True)
    distributor_tax = models.FloatField(
        "Tarifa da Distribuidora", blank=True, null=True
    )
    #  create the foreign key for discount rule model here


# TODO: Create the model DiscountRules below
class DiscountRules(models.Model):
    # Tipos de Consumidor (Consumer Type)
    CONSUMER_TYPES = [
        ('Residencial', 'Residencial'),
        ('Comercial', 'Comercial'),
        ('Industrial', 'Industrial'),
    ]
    
    # Faixa de Consumo (Consumption Range)
    CONSUMPTION_RANGES = [
        ('Baixo', 'Baixo'),
        ('Médio', 'Médio'),
        ('Alto', 'Alto'),
    ]
    
    # Valor de Cobertura (Cover Value)
    COVER_VALUES = [
        ('Baixo', 'Baixo'),
        ('Médio', 'Médio'),
        ('Alto', 'Alto'),
    ]
    
    # Campos do Modelo
    consumer_type = models.CharField(max_length=20, choices=CONSUMER_TYPES)
    consumption_range = models.CharField(max_length=10, choices=CONSUMPTION_RANGES)
    cover_value = models.CharField(max_length=10, choices=COVER_VALUES)
    discount_value = models.FloatField()

    def __str__(self):
        return f"{self.consumer_type} - {self.consumption_range} - {self.cover_value}"

# TODO: You must populate the consumer table with the data provided in the file consumers.xlsx
#  and associate each one with the correct discount rule
