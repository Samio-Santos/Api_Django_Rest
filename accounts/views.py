from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from accounts.facad_accounts import *
from .models import CostumerUser
from rest_framework.authtoken.models import Token


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts_templates/login.html')

    usuario = request.POST.get('user')
    senha = request.POST.get('password')
    user = auth.authenticate(request, username=usuario, password=senha)
    modelUser = get_user_model()
    try:
        # Verifica se o usuario fez cadastro com alguma rede social
        rede_social = modelUser.objects.get(email=usuario)
        # Verifica se o username é diferente do email
        # Caso seja TRUE, então essa condição sera executada
        if rede_social.username != rede_social.email:
            messages.error(
                request, 'Esta conta está vinculada a um rede social abaixo!')
            return render(request, 'accounts_templates/login.html', {'notUser': 'notUser'})

        if not user:
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'accounts_templates/login.html', {'invalid': 'invalid'})

        else:
            auth.login(request, user)
            messages.success(
                request, f'Seja bem-vindo(a) {user.first_name} {user.last_name}!')
            return redirect('index')

    except modelUser.DoesNotExist:
        messages.error(request, 'Usuário não está cadastrado!')
        return render(request, 'accounts_templates/login.html', {'notUser': 'notUser'})


def logout(request):
    auth.logout(request)
    return redirect('login')


def register(request):
    if request.method != 'POST':
        return render(request, 'accounts_templates/register.html')

    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('password')
    rsenha = request.POST.get('Rsenha')

    # Variaveis para vericar se a senha possui pelo menos:
    # uma letra maiuscula
    # uma letra minuscula
    # um numero.
    lower = any(chr.islower() for chr in senha)
    capital = any(chr.isupper() for chr in senha)
    numeric = any(chr.isnumeric() for chr in senha)

    if not get_validacao_dados_register(request=request, nome=nome, email=email, senha=senha, rsenha=rsenha, capital=capital, lower=lower, numeric=numeric):
        return render(request, 'accounts_templates/register.html')

    else:
        messages.success(
            request, 'Usuário registrado com sucesso. Agora faça login!')
        user = CostumerUser.objects.create_user(
            username=email, email=email,  password=senha, first_name=nome)

        user.save()

        return redirect('login')

@login_required(redirect_field_name='#usu@rio$', login_url='login')
def dashboard(request):
    data = {}
    token = Token.objects.filter(user=request.user)

    data['token'] = token[0]
    
    return render(request, 'accounts_templates/index.html', data)


def locked(request):
    return render(request, 'accounts_templates/locked.html')


def Reset_Password_Complete(request):
    messages.success(request, 'Sua senha foi redefinida com SUCESSO!')
    return redirect('login')
