from django.db import models
from django.contrib.auth.models import AbstractUser
from localflavor.br.models import BRCPFField, BRPostalCodeField, BRStateField

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=100, blank=False)
    procfile_photo = models.ImageField(upload_to='procfile', blank=True)
    cpf = BRCPFField('CPF', blank=False)
    cep = BRPostalCodeField('CEP', blank=False)
    state = BRStateField('State', blank=False)
    city = models.CharField(max_length=150, blank=False)
    address = models.CharField(max_length=150, blank=False)
    district = models.CharField(max_length=150, blank=False)
    number = models.CharField(max_length=50, blank=False)
    complement = models.CharField(max_length=150, blank=True)

