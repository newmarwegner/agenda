from django.http import Http404
from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator
from .models import Contato
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
# Create your views here.
def contato(request):
    contatos = Contato.objects.order_by('id').filter(mostrar=True)
    paginator = Paginator(contatos, 10)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    
    return render(request,'contatos.html', {'contatos': contatos})

def ver_contato(request,contato_id):
    contato = get_object_or_404(Contato,id=contato_id)
    
    if not contato.mostrar:
        raise Http404()
        
    return render(request,'detalhes.html', {'contato': contato})


def busca(request):
    termo = request.GET.get('termo')
    
    if termo is None or not termo:
        messages.add_message(request,
                            messages.ERROR,
                            'Campo termo não pode ficar vazio')
        
        return redirect('/')
    
    
    
    campos = Concat('nome',Value(' '),'sobrenome')
    contatos = Contato.objects.annotate(nome_completo = campos).filter(
        Q(nome_completo__icontains = termo) | Q(telefone__icontains = termo),
        mostrar=True)
    
    paginator = Paginator(contatos, 10)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    
    messages.add_message(request,
                        messages.SUCCESS,
                        'Busca realizada')
    
    
    return render(request,'busca.html', {'contatos': contatos})
