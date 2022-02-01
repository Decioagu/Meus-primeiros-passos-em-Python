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

print(f'{azul_claro}={limpar}'*28)
print(f'{azul_claro}={verde_claro} DICIONÁRIO JOGO DE DADOS {azul_claro}={limpar}')
print(f'{azul_claro}={limpar}'*28)
#print(len('DICIONÁRIO JOGO DE DADOS')+4)


from time import sleep
from  random import randint
from operator import itemgetter

sorteio = dict(jogador_1=randint(1, 6),
jogador_2=randint(1, 6),
jogador_3=randint(1, 6),
jogador_4=randint(1, 6))
ranking = []

print()
print('Os valores sorteados são:')
for k, v in sorteio.items():
    print(f'{k} turou {v} no dado')
    sleep(0.5)

print(sorteio)
ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)
print('== RANKIG DOS JOGADORES ==')
for k, v  in enumerate(ranking):
    print(f' {k+1}º lugar {v[0]} com {v[1]}')
    sleep(0.5)
