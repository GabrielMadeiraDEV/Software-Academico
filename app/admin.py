from django.contrib import admin
from .models import Cidade, Ocupacao, Pessoa, Instituicao, AreaSaber, Curso, PeriodoCurso, Disciplina, Matricula, Avaliacao, Frequencia, Turma, Ocorrencia, DisciplinaCurso, TipoAvaliacao

# Registro dos modelos no Django Admin
admin.site.register(Cidade)
admin.site.register(Ocupacao)
admin.site.register(Pessoa)
admin.site.register(Instituicao)
admin.site.register(AreaSaber)
admin.site.register(Curso)
admin.site.register(PeriodoCurso)
admin.site.register(Disciplina)
admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Turma)
admin.site.register(Ocorrencia)
admin.site.register(DisciplinaCurso)
admin.site.register(TipoAvaliacao)

from django.contrib import admin
from .models import Pessoa, Cidade, Ocupacao


admin.site.unregister(Pessoa)  # Desregistra, se necessário
admin.site.unregister(Cidade)  # Desregistra Cidade, se necessário
admin.site.unregister(Ocupacao)  # Desregistra Ocupacao, se necessário

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email', 'cidade', 'ocupacao')  # Campos a serem exibidos na listagem
    search_fields = ('nome', 'cpf', 'email')  # Campos pesquisáveis

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'uf')  # Campos a serem exibidos na listagem

@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)  # Campos a serem exibidos na listagem
