from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_cryptography.fields import encrypt

class Profile(models.Model): #Creates profile in database
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} Profile'

class Card(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    numero = models.CharField(max_length=16)  # Número do cartão de crédito
    validade = models.DateField() # Data de validade do cartão
    titular = models.CharField(max_length=100) # Nome do titular do cartão
    cvv =  models.CharField(max_length=3)

    def get_absolute_url(self):
        return reverse('profile')