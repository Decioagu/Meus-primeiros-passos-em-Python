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


def titulo(txt):
    print(f'{azul_claro}={limpar}' * (len(txt) + 4))
    print(f'{azul_claro}={verde_claro} {txt} {azul_claro}={limpar}')
    print(f'{azul_claro}={limpar}' * (len(txt) + 4))


def mxm(l, c):
    area = l * c
    print(f'A área de um terreno {verde_claro}{l}{limpar} '
          f'x {verde_claro}{c}{limpar} é de '
          f'{verde_claro}{area:.2f}m²{limpar}.')


# PROGRAMA PRINCIPAL
titulo('área'.upper())
print()
largura = float(input('Largura (m): '))
comprimento = float(input('Altura (m): '))
print()
mxm(largura, comprimento)
