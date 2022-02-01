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

print('{}{}{}'.format(azul,'{:=^40}',limpa).format('{}Sequência de Fibonacci{}').format(roxo, azul))
sf = int(input('Quantos termos você deseja mostrar? '))
cont = 0
lista = [0, 1]
while sf > cont:
    lista.append(lista[-1]+lista[-2])
    cont += 1
lista.pop()
lista.pop()
print('{1}Sequência de Fibonacci{0} = {2}{3}{0}'.format(limpa, roxo, azul, lista))

