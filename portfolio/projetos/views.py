from django.shortcuts import render, get_object_or_404
from .models import Projeto


def index(request):
    return render(request, 'projetos/index.html')


def projetos(request):
    projetos = Projeto.objects.all()
    #  {
    #    1: 'Usando Selenium em Python 3',
    #    2: 'Usando dicionários em Python 3',
    #    3: 'Usando listas em Python 3',
    #    4: 'API de clima/temperatura'
    # }

    dados = {
        'projetos': projetos,
    }

    return render(request, "projetos/projetos.html", dados)


def projeto_detalhes(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    dados = {
        'projeto': projeto
    }

    return render(request, "projetos/projeto_detalhes.html", dados)
