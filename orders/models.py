from django.db import models
from model_utils.models import TimeStampedModel
from localflavor.br.models import BRCPFField, BRPostalCodeField, BRStateField
from django.contrib.auth import get_user_model

# Create your models here.
class Order(TimeStampedModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    cpf = BRCPFField('CPF', blank=False)
    cep = BRPostalCodeField('CEP', blank=False)
    state = BRStateField('State', blank=False)
    city = models.CharField(max_length=150, blank=False)
    address = models.CharField(max_length=150, blank=False)
    district = models.CharField(max_length=150, blank=False)
    number = models.CharField(max_length=50, blank=False)
    complement = models.CharField(max_length=150, blank=True)
    is_sent = models.BooleanField(default=False)
    tracker = models.CharField(max_length=150, blank=True)


    class Meta:
        ordering = ['-created']


    def __str__(self):
        return f'{self.username} Order'


class Item(TimeStampedModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.FloatField(max_length=10)
