from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class Usuario(models.Model):
    nome = models.TextField(max_length=255)
    telefone = models.CharField(max_length = 11)
    email = models.EmailField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
