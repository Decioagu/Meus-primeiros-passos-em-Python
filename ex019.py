# Sorteando um item na lista
from random import choice, choices
n0 = input('Digite o primeiro nome: ')
n1 = input('Digite o segundo nome: ')
n2 = input('Digite o terceiro nome: ')
n3 = input('Digite o quarto nome: ')
lista = [n1, n1, n2, n3]
print('O aluno escolhido foi {}.'.format(choice(lista)))
# print('O aluno escolhido foi {}.'.format(choices(lista)))
