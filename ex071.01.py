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
cinquenta = saque // 50
restocinquenta = saque % 50
vinte = restocinquenta // 20
restovinte = restocinquenta % 20
dez = restovinte // 10
restodez = restovinte % 10
um = restodez // 1
if cinquenta > 0:
    print(f'Total de {verde}{cinquenta}{limpar} CÉDULAS de {verde_claro}R$50{limpar}')
if vinte > 0:
    print(f'Total de {verde}{vinte}{limpar} CÉDULAS de {verde_claro}R$20{limpar}')
if dez > 0:
    print(f'Total de {verde}{dez}{limpar} CÉDULAS de {verde_claro}R$10{limpar}')
if um > 0:
    print(f'Total de {verde}{um}{limpar} CÉDULAS de {verde_claro}R$1{limpar}')
print()
print(f'{vermelho_claro}Fim...{limpar}')

