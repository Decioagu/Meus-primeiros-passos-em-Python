# Variáveis de Class e variáveis de instância

class Estudante:
    escola = 'Descomplica'  # variáveis de class

    def __init__(self, nome, matricula):
        self.nome = nome  # variáveis de instância
        self.matricula = matricula  # variáveis de instância

    def __str__(self):
        return f'{self.nome}, número de matricula ({self.matricula}) estuda na escola {self.escola}'

aluno01 = Estudante('Décio', 5699)
aluno02 = Estudante('Ana Rosa', 2018)
print(aluno01)
print(aluno02)
print(f'{aluno01.nome} | {aluno02.nome}')
aluno01.nome = 'Luana'  # alteração variáveis de instância
print(f'{aluno01.nome} | {aluno02.nome}')
Estudante.escola = 'Curso em Video'  # alteração variáveis de class
print(aluno01)
print(aluno02)