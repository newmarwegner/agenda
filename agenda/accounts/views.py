from django.shortcuts import render
from django.contrib import messages
from django.core.validators import validate_email
# Create your views here.

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

   
def cadastro(request):
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')
    
    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request,'Campos faltantes')
        
        return render(request,'cadastro.html')

    if not senha == senha2:
        messages.error(request,'Senhas não conferem')
        
        return render(request,'cadastro.html')
    
    # try:
    #     validate_email(email)
    # except:
    #     messages.error(request,'Email inválido')
    #     return render(request,'cadastro.html')

    
    messages.success(request,'Cadastro realizado com sucesso.')

    return render(request, 'cadastro.html')

def dashboard(request):
    return render(request, 'dashboard.html')
