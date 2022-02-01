# TABELA DE CORES
limpar = '\033[m'
preto = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'
cinza = '\033[37m'
vermelho_claro = '\033[91m'
verde_claro = '\033[92m'
amarelo_claro = '\033[93m'
azul_claro = '\033[94m'
rosa = '\033[95m'
ciano_claro = '\033[96m'
branco = '\033[97m'
sub = '\033[4m'
neg = '\033[1m'
inv = '\033[7m'
# FIM DA TABELA DE CORES

print(f'{azul_claro}={limpar}'*29)
print(f'{azul_claro}={verde_claro} Palpites para a Mega Sena {azul_claro}={limpar}')
print(f'{azul_claro}={limpar}'*29)
#print(len('Palpites para a Mega Sena')+4)

from random import randint
from time import sleep
sorteio = []
cont = 0

print()
while True:
    quant = input(f'Quantos jogos vecê deseja sortea? ').strip()
    if quant.isnumeric() == True:
        quant = int(quant)
        print()
        break
    else:
        print(f'{vermelho_claro}Caracter invalido!{limpar}')
        print(f'{amarelo_claro}Favor digitar apenas valores númericos inteiros.{limpar}')
        print()

for q in range(0, quant):
    for s in range(0, 6):
        while True:
            s = randint(1, 60)
            if s not in sorteio:
                sorteio.append(s)
                break
    cont += 1
    if cont == 1:
        print('{1}{2:$^42}{0}'.format(limpar, verde_claro, f' {azul_claro}JOGOS SORTEADOS{verde_claro} '))
        sleep(1)
    sorteio.sort()
    print(f'{verde}Jogo {cont}{limpar}: {roxo}{sorteio}{limpar}')
    sleep(1)
    sorteio.clear()
print('{1}{2:$^42}{0}'.format(limpar, verde_claro, f' {azul_claro}BOA SORTE{verde_claro} '))

