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

print(f'{azul_claro}={limpar}'*32)
print(f'{azul_claro}={verde_claro} CONTANDO VOGAIS EM UMA TUPLA {azul_claro}={limpar}')
print(f'{azul_claro}={limpar}'*32)
print()

tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO','GRATIS',
'ESTUDAR', 'PRATICAR','TRABALAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
cont = 0
fim = 1

for palavra in tupla:
    print('Na palavra ', end='')
    print(f'{verde_claro}{palavra}{limpar}', end=' temos ')
    palavra = palavra.lower()

    for letra in palavra:
        if letra in ('a', 'e', 'i', 'o', 'u'):
            cont += 1

    for letra in palavra:
        if letra in ('aeiou'):
            print(f'{azul_claro}{letra}{limpar}', end='')
            if fim != cont:
                print(end=', ')
                fim += 1
            else:
                print('.', end='')
                cont = 0
                fim = 1
    print()