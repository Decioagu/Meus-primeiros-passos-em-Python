limpa = '\033[m'
preto = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'
sub = '\033[4m'
negrito = '\033[1m'

from random import randint
from time import sleep

print('\033[36m-=-\033[m' * 10)
print('{:^36}'.format('{}JO{}KEN{}PÔ{}').format(azul, amarelo, vermelho, limpa))
print('\033[36m-=-\033[m' * 10)
print()

lista = ['{}PEDRA{}'.format(ciano, limpa), '{}PAPEL{}'.format(verde, limpa),
         '{}TESOURA{}'.format(roxo, limpa)]
computador = randint(0, 2)

print('Escolha um número abaixo:'.upper())
print('[{0}1{1}] = para {0}PEDRA{1}'.format(ciano, limpa))
print('[{0}2{1}] = para {0}PAPEL{1}'.format(verde, limpa))
print('[{0}3{1}] = para {0}TESOURA{1}'.format(roxo, limpa))
jogador = int(input('Digite um número conforme opção acima: '.upper()))

print()
print(' ' * 10, end='')
print('{}JO{}'.format(azul, limpa), end='')
sleep(1)
print('{}KEN{}'.format(amarelo, limpa), end='')
sleep(1)
print('{}PÔ{}'.format(vermelho, limpa), end='')
sleep(1)
print()

if 0 < jogador <= 3:
    if jogador == 1:
        jogador = lista[0]
        if computador == 0:
            x = '{}HOUVE EMPATE{}'.format(amarelo, limpa)
        elif computador == 1:
            x = '{}COMPUTADOR VENCEU!!!{}'.format(vermelho, limpa)
        elif computador == 2:
            x = '{}VOCÊ VENCEU!!!{}'.format(azul, limpa)
    elif jogador == 2:
        jogador = lista[1]
        if computador == 0:
            x = '{}VOCÊ VENCEU!!!{}'.format(azul, limpa)
        elif computador == 1:
            x = '{}HOUVE EMPATE{}'.format(amarelo, limpa)
        elif computador == 2:
            x = '{}COMPUTADOR VENCEU!!!{}'.format(vermelho, limpa)
    elif jogador == 3:
        jogador = lista[2]
        if computador == 0:
            x = '{}COMPUTADOR VENCEU!!!{}'.format(vermelho, limpa)
        elif computador == 1:
            x = '{}VOCÊ VENCEU!!!{}'.format(azul, limpa)
        elif computador == 2:
            x = '{}HOUVE EMPATE{}'.format(amarelo, limpa)
    print()
    print('{}COMPUTADOR{} jogou "{}"'.format(vermelho, limpa, lista[computador]))
    print('{}VOCÊ{} jogou "{}"'.format(azul, limpa, jogador))
    print(x)
    print()
    print('{0}Fim {1}de {2}jogo{0}.{1}.{2}.{3}'.format(azul, amarelo,
                                                       vermelho, limpa))
else:
    print()
    print('{}Opção invalida!!!'.format(roxo))
    print('{0}Fim {1}de {2}jogo{0}.{1}.{2}.{3}'.format(azul, amarelo,
                                                       vermelho, limpa))
