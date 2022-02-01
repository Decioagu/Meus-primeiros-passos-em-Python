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
print()
print('{}NÚMERO PRIMO{}'.format(verde, limpa))
print()
n = int(input('Digite um {}número inteiro{}: '.format(sub,limpa)))
print()
primo = 0
if n >=2:
    if n == 2:
        print('Número {1}{2}{0}, é {1}PRIMO{0}!!!'.format(limpa, verde, n))
    else:
        for c in range(2,n):
            teste = n % c
            if teste == 0:
                primo += 1
        if primo == 0:
            print('Número {1}{2}{0}, é {1}PRIMO{0}!!!'.format(limpa, verde, n))
        else:
            print('Número {1}{3}{0}, {1}{2}NÃO é PRIMO{0}!!!'.format(limpa, verde, vermelho, n))
else:
    print('Número {3}{4}{0} {2}inválido{0}, digite um número {1}{2}maior{0} '
          'ou {1}{2}igual{0} a "{1}2{0}".'.format(limpa, verde, sub, vermelho, n))
