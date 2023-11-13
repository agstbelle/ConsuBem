from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

CATEGORIAS_PRODUTO = [
    (1, "Livros"),
    (2, "Roupas"),
    (3, "Eletrônicos"),
    (4, "Bolsas"),
    (5, "Acessórios"),
    (6, "Calçados"),
    (7, "Brinquedos"),
    (8, "Decoração"),
    (9, "Outros")
]

ESTADO_PRODUTO = [
    (1, "Novo"),
    (2, "Seminovo"),
    (3, "Usado")
]

class Usuario(models.Model):
    nome = models.TextField(max_length=255)
    telefone = models.CharField(max_length = 11)
    email = models.EmailField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class produto(models.Model):
    nome_produto = models.TextField(max_length=80)
    categoria = models.PositiveBigIntegerField(default = 9, choices= CATEGORIAS_PRODUTO )
    estado = models.PositiveBigIntegerField(default= 3, choices  =ESTADO_PRODUTO)
    descricao_produto = models.TextField(max_length=500)

