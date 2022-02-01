limpa = '\033[m'
preto = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'
cinza = '\033[37m'
neg = '\033[1m'
sub = '\033[4m'
inv = '\033[7m'

from random import randint
from time import sleep

cp = randint(0,9)
print('{:^72}'.format('{}Jogo da adivinhação{}').format(roxo, limpa))
print('='*70)
print('Digite um número de {1}0{0} à {1}9{0} e veja se é o número que eu estou pensando!'.format(limpa, verde))
print('='*70)
j = 0
cont = 0
while j != cp:
    print()
    j = int(input('{}Digite o número: {}'.format(azul, limpa)))
    print('{}PROCESSANDO...{}'.format(amarelo, limpa))
    sleep(1)
    cont += 1
    print()
    if j == cp:
        print('{1}Você ganhou!{0} \n"{1}{2}{0}" era o número que eu estava pensando.'.format(limpa, verde, cp))
        print('Você precisou de {1}{2} tentativas{0} para descobrir o número.'.format(limpa, amarelo, cont))
    elif 0 < j < 10:
        if j > cp:
            print('{1}Você perdeu!{0} \nEstava pensando em {1}{2}número menor{0}.'.format(limpa, vermelho, sub))
        else:
            print('{1}Você perdeu!{0} \nEstava pensando em {1}{2}número maior{0}.'.format(limpa, vermelho, sub))
    else:
        print('{1}Você perdeu!{0} \nNúmero "{1}{2}{0}" não é valido.'.format(limpa, vermelho, j))

