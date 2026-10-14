from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.listar_projetos, name='listar_projetos'),
    path('projetos/novo/', views.criar_projeto, name='criar_projeto'),
    path('projetos/editar/<int:pk>/', views.editar_projeto, name='editar_projeto'),
    path('projetos/excluir/<int:pk>/', views.excluir_projeto, name='excluir_projeto'),

    path('tarefas/', views.listar_tarefas, name='listar_tarefas'),
    path('tarefas/nova/', views.criar_tarefa, name='criar_tarefa'),
    path('tarefas/editar/<int:pk>/', views.editar_tarefa, name='editar_tarefa'),
    path('tarefas/excluir/<int:pk>/', views.excluir_tarefa, name='excluir_tarefa'),
]