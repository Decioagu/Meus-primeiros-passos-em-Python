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
print(f'{azul_claro}☻{limpar}'*18)
print('{}{:☺^45}{}'.format(azul, f' {limpar}BANCO {vermelho_claro}♥{limpar} SEU {verde_claro}R${azul} ', limpar))
print(f'{azul_claro}☻{limpar}'*18)
print()

saque = int(input(f'Qual o valo do saque? {verde_claro}R${limpar}'))
total = saque
cont = 0
cedula = 50

while True:
    while total >= cedula:
        total -= cedula
        cont += 1
    if cont > 0:
        print(f'Total de {verde_claro}{cont}{limpar} cédulas de {verde_claro}R${cedula}{limpar}')
    if cedula == 50:
        cedula = 20
    elif cedula == 20:
        cedula = 10
    elif cedula == 10:
        cedula = 1
    cont = 0
    if total == 0:
        break
print()
print(f'{vermelho_claro}Fim...{limpar}')