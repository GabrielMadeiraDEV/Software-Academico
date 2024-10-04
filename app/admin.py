from django import forms
from django.contrib import admin
from .models import Categoria, Produto, Pessoa, Cidade, Ocupacao, Instituicao, AreaSaber, Curso, PeriodoCurso, Disciplina, Matricula, Avaliacao, Frequencia, Turma, Ocorrencia, Periodo, TipoAvaliacao,DisciplinaCurso

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Pessoa)
admin.site.register(Cidade)
admin.site.register(Ocupacao)
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
admin.site.register(TipoAvaliacao)

admin.site.unregister(Curso)
class DisciplinaCursoInlineForm(forms.ModelForm):
    class Meta:
        model = DisciplinaCurso
        fields = ['disciplina', 'carga_horaria']
        widgets = {
            'disciplina': forms.Select,  # Exibir como dropdown
        }

# Configuração do inline com o formulário ajustado
class DisciplinaCursoInline(admin.TabularInline):
    model = DisciplinaCurso
    form = DisciplinaCursoInlineForm
    extra = 1  # Quantidade inicial de linhas extras

# Registro de Curso com a Inline de DisciplinaCurso
class CursoAdmin(admin.ModelAdmin):
    inlines = [DisciplinaCursoInline]

admin.site.register(Curso, CursoAdmin)