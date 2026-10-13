from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Projeto
from .forms import ProjetoForm


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

    return render(request, 'core/form.html')

def editar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    form = ProjetoForm(request.POST or None, instance=projeto)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Projeto atualizado com sucesso!')
        return redirect('listar_projetos')

    return render(request, 'projetos/form.html', {
        'form': form,
        'titulo': 'Editar Projeto'
    })


def excluir_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        projeto.delete()
        messages.success(request, 'Projeto excluído com sucesso!')
        return redirect('listar_projetos')

    return render(request, 'projetos/excluir.html', {
        'projeto': projeto
    })