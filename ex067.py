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
n = mult = 0
print('{}Para sair digite um número negativo.{}'.upper().format(vermelho, limpa))
while True:
    n = int(input(f'{azul}Quer ver a tabuada de qual número?{limpa} '))
    print(f'{roxo}_{limpa}' * 35)
    if n < 0:
        break
    for c in range(1,11):
        mult = n * c
        print(f'{verde}{n}{limpa} x {roxo}{c:2}{limpa} = {azul}{mult}{limpa}')
    print(f'{roxo}_{limpa}' * 35)
print(f'{amarelo}Fim do Programa...')
