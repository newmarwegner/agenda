from django.shortcuts import render
from django.contrib import messages
# Create your views here.

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

   
def cadastro(request):
   
     # messages.success(request,'Ola mundo')
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')
    print(nome, sobrenome)
    
    return render(request, 'cadastro.html')

def dashboard(request):
    return render(request, 'dashboard.html')
