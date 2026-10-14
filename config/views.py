from django.shortcuts import render, redirect, get_object_or_404
from core.models import Projeto
from core.forms import ProjetoForm

def listar_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos/listar.html', {
        'projetos': projetos
    })

def criar_projeto(request):
    form = ProjetoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_projetos')

    return render(request, 'projetos/form.html', {
        'form': form
    })