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
# FIM TABELA DE CORES

cont = 0
time = ('Red Bull Bragantino', 'Santos', 'Sport', 'São Paulo',
'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Palmeiras',
'Ceará', 'Chapecoense', 'Corinthians', 'Cuiabá', 'Flamengo', 'Fluminense',
'América-MG', 'Athletico', 'Atlético-GO', 'Atlético-MG', 'Bahia')
x = sorted(time)
print('=' * 60)
print('Lista dos times do brasileirão:')
for c in time:
    print(f'{c}', end='')
    if cont != 19:
        print(', ', end='')
    if cont == 19:
        print('.', end='')
    cont += 1
    if cont % 5 == 0:
        print('')
cont = 0
print('=' * 60)
print('O Chapecoense esta na {}ª posição.'.format(time.index('Chapecoense')+1))
print('=' * 60)
print('Os cincos primeiros times do brasileirão são:')
print(time[:5])
print('=' * 60)
print('Os quatros ultimos times do brasileirão são:')
print(time[-4:])
print('=' * 60)
print('Lista dos times do brasileirão em ordem alfabetica:')
for c in x:
    print(f'{c}', end='')
    if cont != 19:
        print(', ', end='')
    if cont == 19:
        print('.', end='')
    cont += 1
    if cont % 5 == 0:
        print('')
print('=' * 60)
print('O Chapecoense esta na {}ª posição.'.format(x.index('Chapecoense')+1))
print('=' * 60)
