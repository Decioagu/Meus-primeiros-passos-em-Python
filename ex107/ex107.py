# TABELA DE CORES
limpar = '\033[m'
roxo = '\033[35m'
vermelho_claro = '\033[91m'
verde_claro = '\033[92m'
amarelo_claro = '\033[93m'
# FIM DA TABELA DE CORES

import moeda7

moeda7.titulo('Exercitando módulos em Python'.upper())
print()
valor = input(f'Digite o preço: {verde_claro}R${limpar}')
valor = moeda7.teste_float(valor)
print(f'A {roxo}metade{limpar} de {verde_claro}R${valor:.2f}{limpar} é {verde_claro}R${moeda7.metade(valor):.2f}{limpar}')
print(f'A {roxo}dobro{limpar} de {verde_claro}R${valor:.2f}{limpar} é {verde_claro}R${moeda7.dobro(valor):.2f}{limpar}')
print(f'{roxo}Aumento{limpar} de {amarelo_claro}10%{limpar} de {verde_claro}R${valor:.2f}{limpar} é {verde_claro}R${moeda7.aumentar(valor):.2f}{limpar}')
print(f'{roxo}Redução{limpar} de {amarelo_claro}10%{limpar} de {verde_claro}R${valor:.2f}{limpar} é {verde_claro}R${moeda7.diminuir(valor):.2f}{limpar}')
