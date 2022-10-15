# Método de class e Método estático

import datetime
# Class
class Pessoa:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano

    @classmethod  # método de classe
    def sua_idade(cls, nome, ano_nascimento, sexo):
        ano_atual = datetime.date.today().year
        idade = ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod  # método de estático
    def maior_idade(idade):
        return idade >= 18


pessoa = Pessoa.sua_idade('Décio Santana de Aguiar', 1981, 'M')
print(pessoa.nome, pessoa.ano)
print(Pessoa.maior_idade(21))
print(Pessoa.maior_idade(12))
