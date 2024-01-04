from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Perfil, Produto, Ecobag, Solicitar_troca
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

def index(request):
    return render(request, 'index.html')

def troca_item(request):
    return render(request, 'troca_item.html')

def cadastro(request):
    if request.POST:
        senha = request.POST.get('senha')
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        perfil = Perfil.objects.filter(user__username=email).first()
        
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Endereço de e-mail já cadastrado.')
            return render(request, 'cadastro.html')

        # Verificar se o e-mail já está em uso por um objeto Usuario
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Endereço de e-mail já cadastrado.')
            return render(request, 'cadastro.html')

        # Se o usuário e e-mail não existirem, criar um novo usuário
        user = User(username=email, email=email, password=senha, is_staff= False)
        user.set_password(senha)
        user.save()
        perfil= Perfil(nome=nome, telefone=telefone, user=user)
        perfil.save()
        messages.success(request, 'Cadastro realizado com sucesso.')
        return redirect('login')
        
    return render(request, 'cadastro.html')

        #if usuario is None:
  
            #user = User.objects.create_user(username=email, email=email, password=senha)
            #user.save()
            #usuario = Usuario(nome=nome, telefone=telefone, user=user)
            #usuario.save()
            #messages.success(request, 'Cadastro realizado com sucesso.')
            #print(messages)
            #return redirect('login')

        #else:
            #print("Usuário já cadastrado")
            #messages.error(request, 'Endereço de e-mail já cadastrado.')
            #return render(request, 'cadastro.html')
            
        
    return render(request, 'cadastro.html')

def user_login(request):
    if request.POST:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(request, username=username, password=senha)
        print(username, senha)
        if user is not None:
            login(request, user)
            p_logado = Perfil.objects.filter(user__id = user.id ) 
            if user.is_staff:
                return redirect("dashboard")
            else:
                return redirect("index")
        else:
            messages.error(request, 'usuário ou senha incorretos')
            return render(request, 'login.html')

    return render(request, 'login.html')

def ecobag(request):
    return render(request, 'ecobag.html')

def dashboard_admin(request):
    return render(request, 'dashboard_admin.html')

def cadastro_admin(request):
    return render(request, 'cadastrar_admin.html')

def cadastro_produto(request):
    if request.POST:
        np = request.POST.get('nome_produto')
        dp = request.POST.get('descricaoProduto')
        cp = request.POST.get('categoria')
        ecp = request.POST.get('estado')
        fto = request.FILES['foto_produto']
        
        novo = Produto(nome_produto= np, descricao_produto = dp, categoria = cp, estado = ecp, foto_produto = fto)
        novo.ativo = True
        novo.user= request.user
        novo.save()
        messages.success(request, 'Produto cadastrado com sucesso.')
    else:
        print("deu errado")
    
    return render(request, 'cadastrar_produto.html')

# views.py
def cadastro_admin(request):
    if request.POST:
        senha = request.POST.get('senha_adm')
        nome = request.POST.get('nome_adm')
        matricula = request.POST.get('matricula')
        email = request.POST.get('email_adm')
        print (matricula,email,senha)
        
        if User.objects.filter(username=matricula).exists():
            messages.error(request, 'Matrícula já cadastrada.')
            return render(request, 'cadastrar_admin.html')
        
        # Verificar se o e-mail já está em uso por um objeto UsuarioAdministrador
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Endereço de e-mail já cadastrado.')
            return render(request, 'cadastrar_admin.html')

        # Se o usuário e e-mail não existirem, criar um novo usuário administrador
        user = User(username=matricula, email=email, password=senha, is_staff = True )
        user.set_password(senha)
        user.save()
        admin_user = Perfil(nome=nome, matricula=matricula, user=user)
        admin_user.save()
        messages.success(request, 'Cadastro de administrador realizado com sucesso.')
        return redirect('login')
        
    return render(request, 'cadastrar_admin.html')

def produtos(request, categoria):
    if categoria != 0:
        produtos =  Produto.objects.filter(ativo = True, categoria = categoria)
    else:
        produtos =  Produto.objects.filter(ativo = True)

    ecobag = []

    ctx = {
        'lista' : produtos,
        
    }

    
    return render (request, "catalogo.html", ctx)

@login_required
def ecobag(request):

    ecobag_items = Ecobag.objects.filter(usuario=request.user)
    
    ctx = {
        'lista': ecobag_items,
    }
        
    return render(request, "ecobag.html", ctx)

    """ecobag = []
    if request.user.is_authenticated:
        ecobag = Ecobag(usuario=request.user)

        ctx = {
            'lista' : ecobag,
            }
            
        return render (request, "ecobag.html", ctx)"""
   

def add_ecobag(request, id):
    produto = get_object_or_404(Produto, pk=id)

    if request.user.is_authenticated:
        # Verifique se o produto já está na Ecobag
        if Ecobag.objects.filter(usuario=request.user, produto=produto).exists():
            messages.warning(request, 'Este produto já está na sua Ecobag.')
        else:
            # Adicione o produto à Ecobag
            ecobag_item = Ecobag(usuario=request.user, produto=produto)
            ecobag_item.save()
            messages.success(request, 'Produto adicionado à Ecobag com sucesso.')

        #return redirect(f'/produtos/{produto.categoria}')
        return redirect('ecobag')

    else:
        return redirect('login')
    
def solicitar_troca(request):
    if request.POST:
        nt = request.POST.get('nome_troca')
        dt = request.POST.get('descricao_troca')
        ct = request.POST.get('categoria_troca')
        ect = request.POST.get('estado_troca')
        ftot = request.FILES['foto_troca']
        
        novo = Solicitar_troca(nome_troca= nt, descricao_troca = dt, categoria_troca = ct, estado_troca = ect, foto_troca = ftot)
        novo.ativo = False
        novo.user= request.user
        novo.save()
        messages.success(request, 'troca solicitada')
    else:
        print("deu errado")
    
    return render (request, 'troca_item.html')


   
    
    












 






