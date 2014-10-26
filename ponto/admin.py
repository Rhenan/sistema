from django.contrib import admin

# Register your models here.

from ponto.models import Aluno


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'matricula')

admin.site.register(Aluno, AlunoAdmin)