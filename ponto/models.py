from django.db import models

# Create your models here.

class Aluno(models.Model):
    id = models.IntegerField(primary_key=True)
    matricula = models.IntegerField()
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    nascimento = models.DateField()
    pai = models.CharField(max_length=100)
    mae = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=10)
    endereco = models.CharField(max_length=300)

class Coordenador(models.Model):
    id = models.IntegerField(primary_key=True)
    matricula = models.IntegerField()
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    nascimento = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=10)
    endereco = models.CharField(max_length=300)

class Cursinho(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=10)
    endereco = models.CharField(max_length=300)
    aluno_id = models.ForeignKey(Aluno)
    coordenador_id = models.ForeignKey(Coordenador)


