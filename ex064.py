limpa = '\033[m'
preto = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'
cinza = '\033[37m'
sub = '\033[4m'
neg = '\033[1m'
inv = '\033[7m'
n = cont = soma = 0
n = int(input('Digite um número inteiro {}[999 PARA PARAR]{}: '.format(vermelho, limpa)))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número inteiro {}[999 PARA PARAR]{}: '.format(vermelho, limpa)))
print('Você digitou {1}{3}{0} números e a soma entre eles foi {2}{4}{0}!'.format(limpa, amarelo, verde, cont, soma))
