from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Projeto, Tarefa
from .forms import ProjetoForm, TarefaForm


def listar_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'core/listar.html', {
        'projetos': projetos
    })


def criar_projeto(request):
    form = ProjetoForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Projeto cadastrado com sucesso!')
        return redirect('listar_projetos')

    return render(request, 'core/form.html')

def editar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    form = ProjetoForm(request.POST or None, instance=projeto)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Projeto atualizado com sucesso!')
        return redirect('listar_projetos')

    return render(request, 'core/form.html', {
        'form': form,
        'titulo': 'Editar Projeto'
    })


def excluir_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        projeto.delete()
        messages.success(request, 'Projeto excluído com sucesso!')
        return redirect('listar_projetos')

    return render(request, 'core/excluir.html', {
        'projeto': projeto
    })

def listar_tarefas(request):
    tarefas = Tarefa.objects.select_related('projeto').all()

    return render(request, 'tarefas/listar.html', {
        'tarefas': tarefas
    })


def criar_tarefa(request):
    form = TarefaForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Tarefa cadastrada com sucesso!')
        return redirect('listar_tarefas')

    return render(request, 'tarefas/form.html', {
        'form': form,
        'titulo': 'Cadastrar Tarefa'
    })


def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    form = TarefaForm(request.POST or None, instance=tarefa)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Tarefa atualizada com sucesso!')
        return redirect('listar_tarefas')

    return render(request, 'tarefas/form.html', {
        'form': form,
        'titulo': 'Editar Tarefa'
    })


def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('listar_tarefas')

    return render(request, 'tarefas/excluir.html', {
        'tarefa': tarefa
    })