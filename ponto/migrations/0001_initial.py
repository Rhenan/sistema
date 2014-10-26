# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('matricula', models.IntegerField()),
                ('nome', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=1)),
                ('nascimento', models.DateField()),
                ('pai', models.CharField(max_length=100)),
                ('mae', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('telefone', models.CharField(max_length=10)),
                ('endereco', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Coordenador',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('matricula', models.IntegerField()),
                ('nome', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=1)),
                ('nascimento', models.DateField()),
                ('email', models.EmailField(max_length=75)),
                ('telefone', models.CharField(max_length=10)),
                ('endereco', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cursinho',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=10)),
                ('endereco', models.CharField(max_length=300)),
                ('aluno_id', models.ForeignKey(to='ponto.Aluno')),
                ('coordenador_id', models.ForeignKey(to='ponto.Coordenador')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
