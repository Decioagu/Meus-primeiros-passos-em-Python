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
from random import randint
print()
tupla = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))
print(f'Os valores sorteados foram: {amarelo_claro}{tupla}{limpar}')
print(f'O {vermelho_claro}maior{limpar} valor foi: {vermelho_claro}{max(tupla)}{limpar}')
print(f'O {ciano}menor{limpar} valor foi: {ciano}{min(tupla)}{limpar}')