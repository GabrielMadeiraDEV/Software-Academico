from django.urls import path
from .views import *
urlpatterns = [
path('', IndexView.as_view(), name='index'),
path('pessoas', PessoasView.as_view(), name='pessoas'),
path('cursos', CursosView.as_view(), name='cursos'),
path('instituiçoes', InstituicoesView.as_view(), name='instituicoes'),
path('ocupacoes', OcupacoesView.as_view(), name='ocupacoes'),
path('disciplinas', DisciplinasView.as_view(), name='disciplinas'),
path('matriculas', MatriculasView.as_view(), name='matriculas'),
path('cadastrar_pessoa', CadastrarPessoaView.as_view(), name='cadastrar_pessoa'),
path('gerenciar_pessoas', GerenciarPessoasView.as_view(), name='gerenciar_pessoas'),
path('deletar_pessoa/<int:id>', DeletarPessoasView.as_view(), name='deletar_pessoa'),
]
