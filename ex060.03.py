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
from math import factorial
print('{}{}{}'.format(azul,'{:=^40}',limpa).format('{}Calculo fatorial{}').format(verde, azul))
num = int(input('Digite um valor numérico inteiro: '))
fatorial = factorial(num)
print('{1}{3}!{0} = {2}{4}{0}'.format(limpa, verde, azul, num, fatorial))
