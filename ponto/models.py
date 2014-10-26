from django.db import models

# Create your models here.

class Aluno(models.Model):
    id = models.IntegerField(primary_key=True)
    matricula = models.IntegerField()
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    nascimento = models.DateField()
    pai = models.CharField()
    mae = models.CharField()
    email = models.EmailField()
    telefone = models.CharField(max_length=10)
    endereco = models.CharField()

class Coordenador(models.Model):
    id = models.IntegerField(primary_key=True)
    matricula = models.IntegerField()
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    nascimento = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=10)
    endereco = models.CharField()

class Cursinho(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=10)
    endereco = models.CharField()
    aluno_id = models.ManyToOneRel(Aluno.id)
    coordenador_id = models.ManyToOneRel(Coordenador.id)


