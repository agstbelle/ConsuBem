from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Usuario
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    if request.POST:
        senha = request.POST.get('senha')
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        usuario = Usuario.objects.filter(user__username=email).first()

        if usuario is None:
  
            user = User.objects.create_user(username=email, email=email, password=senha)
            user.save()
            usuario = Usuario(nome=nome, telefone=telefone, user=user)
            usuario.save()
            messages.success(request, 'Cadastro realizado com sucesso.')
            return redirect('login')

        
        else:
            messages.error(request, "Usuário já cadastrado")
            return render(request, 'cadastro')
            #messages.error(request, 'Usuário já cadastrado.')
            #return render(request, 'cadastro.html')
            #return redirect('cadastro')
    return render(request, 'cadastro.html')

def user_login(request):
    if request.POST:
        username = request.POST.get('email')
        senha = request.POST['senha']
        user = authenticate(request, username=username, password=senha)
        print(user, username, senha)
        if user is not None:
            login(request, user)
            #return redirect('index')  # Redirecionar para a página após o login
            return redirect("index")
        else:
            messages.error(request, 'Credenciais inválidas')
            return render(request, 'login.html')

    return render(request, 'login.html')


 





