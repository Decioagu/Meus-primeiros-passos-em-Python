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
print(f'{azul_claro}={verde_claro} EXTRAINDO DADOS DE UMA LISTA {azul_claro}={limpar}')
print(f'{azul_claro}={limpar}'*32)
#print(len('EXTRAINDO DADOS DE UMA LISTA')+4)

print()
cont = contpar = contimpar = 0
opção = ''
lista = []
listapar = []
listaimpar = []
while opção != 'N':
    cont += 1
    while True:
        valor = input(f'Digite o {cont}º valor: ')
        if valor.isnumeric() == True:
            valor = int(valor)
            lista.append(valor)
            break
        else:
            print(f'{vermelho}Caracter invalido!{limpar}')

    while True:
        opção = input(f'Quer continuar? [{amarelo_claro}S{limpar}/{amarelo_claro}N{limpar}]').upper()
        if opção in 'S':
            print()
            break
        elif opção in 'N':
            break
        else:
            print(f'{vermelho_claro}Opção invalida!{limpar}')
            print(f'Digite "{amarelo_claro}S{limpar}" para {amarelo_claro}CONTINUAR{limpar} ou "{amarelo_claro}N{limpar}" para {amarelo_claro}SAIR{limpar}.')

print()
print(f'{verde_claro}Lista = {lista}{limpar}')
for c in lista:
    if c % 2 == 0:
        listapar.append(c)
        contpar += 1
    else:
        listaimpar.append(c)
        contimpar += 1
if contpar != 0:
    print(f'{amarelo_claro}Lista PAR = {listapar}{limpar}')
if contimpar != 0:
    print(f'{vermelho_claro}Lista IMPAR = {listaimpar}{limpar}')
