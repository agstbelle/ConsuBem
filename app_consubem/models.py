from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class CATEGORIAS_PRODUTO(models.TextChoices):
    LIVRO = 1, "Livros"
    ROUPA = 2, "Roupas"
    ELETRONICO = 3, "Eletrônicos"
    BOLSA = 4, "Bolsas"
    ACESSORIO = 5, "Acessórios"
    CALCADO = 6, "Calçados"
    BRINQUEDO = 7, "Brinquedos"
    DECORACAO = 8, "Decoração"
    OUTRO = 9, "Outros"


class ESTADO_PRODUTO(models.TextChoices):
    NOVO = 1, "Novo"
    SEMINOVO = 2, "Seminovo"
    DESGASTADO = 3, "Desgastado"

class Perfil(models.Model):
    nome = models.TextField(max_length=255)
    telefone = models.CharField(max_length = 11)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length = 14, unique=False, null= False)

class Produto(models.Model):
    nome_produto = models.TextField(max_length=80)
    categoria = models.CharField(max_length=80, default = CATEGORIAS_PRODUTO.OUTRO, choices= CATEGORIAS_PRODUTO.choices)
    estado = models.CharField(max_length=80, default = ESTADO_PRODUTO.NOVO, choices= ESTADO_PRODUTO.choices)
    descricao_produto = models.TextField(max_length=500)
    foto_produto =  models.ImageField(upload_to="fotos_produto")
    ativo = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class Ecobag(models.Model):
     usuario = models.ForeignKey(User, on_delete=models.CASCADE)
     produto = models.ForeignKey(Produto, on_delete=models.CASCADE)  

     def __str__(self):
        return f"{self.usuario.username} -  {self.produto.nome_produto}"
     
     




    

