from django import forms
from .models import Projeto, Tarefa

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'data_inicio']

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'prioridade', 'concluido', 'projeto']