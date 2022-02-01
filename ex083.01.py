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

print(f'{azul_claro}={limpar}'*34)
print(f'{azul_claro}={verde_claro} VALIDANDO EXPRESSÃO MATEMÁTICA {azul_claro}={limpar}')
print(f'{azul_claro}={limpar}'*34)
#print(len('Validando expressõe matemática')+4)

cont = 0
express = input(f'Digite uma {amarelo_claro}EXPRESSÃO MATEMÁTICA{limpar}:')
for c in express:
    if c == '(':
        cont += 1
    if c == ')':
        cont -= 1

if cont == 0:
    print(f'Expressão esta {verde_claro}CERTA{limpar}...')
else:
    print(f'Expressão esta {vermelho_claro}ERRADA{limpar}...')


