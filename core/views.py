from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto


def listar_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'core/listar.html', {
        'projetos': projetos
    })


def criar_projeto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        data_inicio = request.POST.get('data_inicio')

        Projeto.objects.create(
            nome=nome,
            descricao=descricao,
            data_inicio=data_inicio
        )

        return redirect('listar_projetos')

    return render(request, 'core/formulario_projeto.html')
