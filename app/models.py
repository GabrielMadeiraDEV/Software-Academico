from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Categorias"
    
    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='static/', blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Produtos"
    
    def __str__(self):
        return f'{self.categoria} {self.nome}'
    
class Pessoa(models.Model):
    nome = models.CharField(max_length=150)
    nome_do_pai = models.CharField(max_length=150, blank=True, null=True)
    nome_da_mae = models.CharField(max_length=150, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True)
    data_nasc = models.DateField()
    email = models.EmailField(unique=True)
    cidade = models.ForeignKey('Cidade', on_delete=models.SET_NULL, null=True, blank=True)
    ocupacao = models.ForeignKey('Ocupacao', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome} ({self.uf})"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Instituicao(models.Model):
    nome = models.CharField(max_length=150)
    site = models.URLField(blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class AreaSaber(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=150)
    carga_horaria_total = models.IntegerField()
    duracao_meses = models.IntegerField()
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.SET_NULL, null=True, blank=True)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class PeriodoCurso(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class Matricula(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()

    def __str__(self):
        return f"{self.pessoa.nome} - {self.curso.nome}"

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=255)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

class Frequencia(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    numero_faltas = models.IntegerField()

    def __str__(self):
        return f"{self.pessoa.nome} - {self.disciplina.nome} ({self.numero_faltas} faltas)"

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    turno = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Ocorrencia(models.Model):
    descricao = models.TextField()
    data = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.data} - {self.descricao}"

class DisciplinaCurso(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    carga_horaria = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.ForeignKey(PeriodoCurso, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.curso.nome} - {self.disciplina.nome}"

class TipoAvaliacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome