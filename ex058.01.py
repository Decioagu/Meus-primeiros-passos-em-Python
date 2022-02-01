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
from random import choice
from time import sleep

lista = range(1,11)
print(lista)
l = choice(lista)
print('-'*25, '{}Jogo da adivinhação{}'.upper().format(roxo, limpa), '-'*25)
print('='*71)
print('Digite um número de {1}1{0} à {1}10{0} e veja se é o número que eu estou pensando!'.format(limpa, verde))
print('='*71)
n = 0
cont = 0
while n != l:
    print()
    n = int(input('{}Digite um número:{} '.format(ciano, limpa)))
    print('{}PROCESSANDO...{}'.format(amarelo, limpa))
    sleep(1)
    cont += 1
    print()
    if n == l:
        print('{1}Você ganhou!{0} \n"{1}{2}{0}" era o número que eu estava pensando.'.format(limpa, verde, n))
        print('Você precisou de {1}{2} tentativas{0} para descobrir o número.'.format(limpa, amarelo, cont))
    elif 0 < n < 11:
        if n > l:
            print('{1}Você perdeu!{0} \nEstava pensando em um {1}{2}número menor{0}.'.format(limpa, vermelho, sub))
        else:
            print('{1}Você perdeu!{0} \nEstava pensando em um {1}{2}número maior{0}.'.format(limpa, vermelho, sub))
    else:
        print('{1}Você perdeu!{0} \nNúmero "{1}{2}{0}" não é valido.'.format(limpa, vermelho, n))
