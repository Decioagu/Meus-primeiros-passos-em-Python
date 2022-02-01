from random import choice
from time import sleep
lista = [0, 1, 2, 3, 4, 5]
l = choice(lista)
print('-'*25, 'Jogo da adivinhação', '-'*25)
print('='*71)
print('Digite um número de 0 à 5 e veja se é o número que eu estou pensando!')
print('='*71)
n = int(input('Digite o número: '))
print('PROCESSANDO...')
sleep(1)
print()
if n < 0 or n > 5:
    print('Você perdeu! \nNúmero "{}" não é valido.'.format(n))
elif n == l:
    print('Você ganhou! \n"{}" era o número que eu estava pensando.'.format(n))
else:
    print('Você perdeu! \nEstava pensando no número "{}".'.format(l))
