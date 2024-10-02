# views.py no seu app
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Pessoa, Cidade, Ocupacao

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        pass

class PessoasView(View):
    def get(self, request):
        pessoas = Pessoa.objects.all()
        cidades = Cidade.objects.all()
        ocupacoes = Ocupacao.objects.all()# Apenas como exemplo para renderizar corretamente
        return render(request, 'pessoas.html', {'pessoas': pessoas, 'cidades': cidades, 'ocupacoes': ocupacoes})

    def post(self, request):
        pass
    
class CursosView(View):
    def get(self, request):
        cursos = []  # Apenas como exemplo para renderizar corretamente
        return render(request, 'cursos.html', {'cursos': cursos})

    def post(self, request):
        pass
    
class InstituicoesView(View):
    def get(self, request):
        instituicoes = []  # Apenas como exemplo para renderizar corretamente
        return render(request, 'instituicoes.html', {'instituicoes': instituicoes})

    def post(self, request):
        pass

class OcupacoesView(View):
    def get(self, request):
        ocupacoes = []  # Apenas como exemplo para renderizar corretamente
        return render(request, 'ocupacoes.html', {'ocupacoes': ocupacoes})

    def post(self, request):
        pass

class MatriculasView(View):
    def get(self, request):
        matriculas = []  # Apenas como exemplo para renderizar corretamente
        return render(request, 'matriculas.html', {'matriculas': matriculas})

    def post(self, request):
        pass
    
class DisciplinasView(View):
    def get(self, request):
        disciplinas = []  # Apenas como exemplo para renderizar corretamente
        return render(request, 'disciplinas.html', {'disciplonas': disciplinas})

    def post(self, request):
        pass
    
class CadastrarPessoaView(View):
    def get(self, request):
        cidades = Cidade.objects.all()
        ocupacoes = Ocupacao.objects.all()
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoas.html', {'pessoas': pessoas, 'cidades': cidades, 'ocupacoes': ocupacoes})

    def post(self, request):
        # Recupera dados do formulário
        nome = request.POST['nome']
        nome_pai = request.POST['nome_pai']
        nome_mae = request.POST['nome_mae']
        cpf = request.POST['cpf']
        data_nasc = request.POST['data_nasc']
        email = request.POST['email']
        cidade = get_object_or_404(Cidade, id=request.POST['cidade'])
        ocupacao = get_object_or_404(Ocupacao, id=request.POST['ocupacao'])
        
        # Cria e salva o objeto Pessoa
        nova_pessoa = Pessoa(
            nome=nome, nome_do_pai=nome_pai, nome_da_mae=nome_mae, 
            cpf=cpf, data_nasc=data_nasc, email=email, cidade=cidade, ocupacao=ocupacao
        )
        nova_pessoa.save()
        
        return redirect('cadastrar_pessoa')
    
class GerenciarPessoasView(View):
    def get(self, request):
        # Recupera todas as pessoas, cidades e ocupações
        pessoas = Pessoa.objects.all()
        cidades = Cidade.objects.all()
        ocupacoes = Ocupacao.objects.all()

        # Renderiza o template com a listagem de pessoas e os dados para o formulário
        return render(request, 'pessoas.html', {
            'pessoas': pessoas,
            'cidades': cidades,
            'ocupacoes': ocupacoes,
            'pessoa': None,  # Inicialmente, não temos uma pessoa para editar
        })

    def post(self, request):
        # Verifica se estamos atualizando uma pessoa
        if 'editar' in request.POST:
            pessoa_id = request.POST['pessoa_id']
            pessoa = get_object_or_404(Pessoa, id=pessoa_id)

            # Atualiza os dados da pessoa com os valores do formulário
            pessoa.nome = request.POST['nome']
            pessoa.nome_do_pai = request.POST['nome_pai']
            pessoa.nome_da_mae = request.POST['nome_mae']
            pessoa.cpf = request.POST['cpf']
            pessoa.data_nasc = request.POST['data_nasc']
            pessoa.email = request.POST['email']
            pessoa.cidade = get_object_or_404(Cidade, id=request.POST['cidade'])
            pessoa.ocupacao = get_object_or_404(Ocupacao, id=request.POST['ocupacao'])
            pessoa.save()

            # Redireciona para a mesma página para evitar o reenvio do formulário
            return redirect('gerenciar_pessoas')  # O nome da URL deve ser ajustado conforme o seu caso

        # Se não for edição, é um cadastro
        # Aqui você pode adicionar a lógica de cadastro de uma nova pessoa, se necessário

        return redirect('gerenciar_pessoas')  # Redireciona para a mesma página
    
class DeletarPessoasView(View):
    def post(self, request, pessoa_id):
        # Recupera a pessoa a ser deletada com base no ID
        pessoa = get_object_or_404(Pessoa, id=pessoa_id)
        
        # Deleta a pessoa
        pessoa.delete()

        # Redireciona para a listagem de pessoas após a exclusão
        return redirect('listar_pessoas')  # Certifique-se de que esta URL está definida em seu urls.py