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
while True:
    n = int(input(f'Digite um número inteiro {vermelho}[999 PARA PARAR]{limpa}:'))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {amarelo}{cont} números{limpa} e a {verde}soma{limpa} entre eles foi {verde}{soma}{limpa}!')
