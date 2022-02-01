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

print('{}{}{}'.format(azul,'{:=^40}',limpa).format('{}Calculo fatorial{}').format(verde, azul))
num = int(input('Digite um valor numérico inteiro: '))
cont = num - 1
fatorial = num
print('{1}{2}!{0} = {2}'.format(limpa, verde, num), end='x')

while cont != 0:
    fatorial = fatorial * cont
    print('{}'.format(cont), end='')
    print('x' if cont > 1 else ' = ', end='')
    cont -= 1
print('{1}{2}{0}'.format(limpa, azul, fatorial))
print('Fatorial de número {1}{3}!{0} = {2}{4}{0}'.format(limpa, verde, azul, num, fatorial))
