# Sorteando uma ordem na lista
import random
n0 = input('Digite o primeiro nome: ')
n1 = input('Digite o segundo nome: ')
n2 = input('Digite o terceiro nome: ')
n3 = input('Digite o quarto nome: ')
lista = [n0, n1, n2, n3]
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)

