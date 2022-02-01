from random import randint
from time import sleep
cp = randint(0, 5)
print('-'*25, 'Jogo da adivinhação', '-'*25)
print('='*71)
print('Digite um número de 0 à 5 e veja se é o número que eu estou pensando!')
print('='*71)
j = int(input('Digite o número: '))
print('PROCESSANDO...')
sleep(1)
print()
if j < 0 or j > 5:
    print('Você perdeu! \nNúmero "{}" não é valido.'.format(j))
elif j == cp:
    print('Você ganhou! \n"{}" era o número que eu estava pensando.'.format(j))
else:
    print('Você perdeu! \nEstava pensando no número "{}".'.format(cp))