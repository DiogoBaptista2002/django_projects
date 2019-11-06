from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Refeicoe(models.Model):
    dia = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=3, decimal_places=2)
    prato = models.TextField(default='Puré de ganso')

    def __str__(self):
        return self.dia


class Comida(models.Model):
    comida = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=3, decimal_places=2)
    descricao = models.TextField(default='Pão barrado com queijo de cabra')

    def __str__(self):
        return self.comida



class CustomUser(AbstractUser, models.Model):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True, editable=True)
    username = models.CharField(max_length=30, unique=True, editable=True)
    balance = models.DecimalField(default=0.0, max_digits=6, decimal_places=2, editable=True)
    marcacoes = models.TextField(default="", editable=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.email





