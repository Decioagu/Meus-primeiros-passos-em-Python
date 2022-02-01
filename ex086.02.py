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

print(f'{azul_claro}={limpar}'*20)
print(f'{azul_claro}={verde_claro} MATRIZ COM LISTA {azul_claro}={limpar}')
print(f'{azul_claro}={limpar}'*20)
#print(len('MATRIZ COM LISTA')+4)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
cont = 0
print()
for linha in range(0, 3):
    for coluna in range(0, 3):
        while True:
            num = input(f'Digite um valor para {verde_claro}[{linha+1}, {coluna+1}]{limpar}: ').strip()
            if num.isnumeric() == True:
                num = int(num)
                break
            else:
                print(f'{vermelho_claro}Caracter invalido!{limpar}')
                print(f'{amarelo_claro}Favor digitar apenas valores númericos inteiros.{limpar}')
                print()
        matriz[linha][coluna] = num

print()
print('{}{}{}'.format(verde_claro, f'MATRIZ'.center(22), limpar))
print(f'{azul_claro}={limpar}'*23)
for l in matriz:
    print(f'{azul_claro}={limpar}',end='')
    for c in l:
        print('{1}[{2:^5}]{0}'.format(limpar, verde_claro, c), end='')
        cont += 1
        if cont == 3:
            cont = 0
            print( f'{azul_claro}={limpar}',end='\n')
print(f'{azul_claro}={limpar}'*23)
