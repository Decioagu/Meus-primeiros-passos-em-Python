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

print('{}{}{}'.format(azul, '{:=^40}', limpa).format('{}Sequência de Fibonacci{}').format(roxo, azul))

sf = int(input('Quantos termos você deseja mostrar? '))
cont = 2
t0 = 0
t1 = 1
tn = 0
print(verde, end='')
if sf == 1:
    print('{}'.format(t0,), end=' → ')
if sf == 2:
    print('{} → {}'.format(t0, t1), end=' → ')
if sf > 2:
    print('{} → {}'.format(t0, t1), end=' → ')
    while sf > cont:
        tn = t0 + t1
        # t0 = t1
        # t1 = tn
        t0, t1 = t1, tn
        print(tn, end=' → ')
        cont += 1
print('FIM')

