import email
from django.db import models

class Formulario(models.Model):
    BANCO ={
        (1, 'BTG Pactual'),
        (2, 'Santanader'),
    }

    POSICAO = {
        (1, 'Long EUR'),
        (2, 'Long USD'), 
        (3, 'Short EUR'),
        (4, 'Short USD'),
    }
    banco = models.CharField(max_length=1, choices=BANCO)
    notional = models.IntegerField()
    taxa_entrada = models.IntegerField()
    posicao = models.CharField(max_length=1, choices=POSICAO)
    businessUnit = models.TextField(max_length=150, blank=True)
    dataRegistro = models.DateField
    usuario = models.CharField(max_length=100)
    modificacao = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()