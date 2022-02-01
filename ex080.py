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

print(f'{azul_claro}={limpar}'*18)
print(f'{azul_claro}={verde_claro} LISTA ORDENADA {azul_claro}={limpar}')
print(f'{azul_claro}={limpar}'*18)
#print(len('LISTA ORDENADA')+4)

print()
maior = menor = 0
lista = []
for valor in range(1, 6):
    print(f'{roxo}lista = {lista}{limpar}')
    num = int(input(f'Digite o {valor}º {verde_claro}NÚMERO{limpar}: '))
    if valor == 1 or num > lista[-1]:
        if len(lista) ==  0:
            print(f'{verde_claro}NÚMERO = {num}{limpar} > {roxo}lista = [VAZIO]{limpar}')
        else:
            print(f'{amarelo_claro}Comparando o ultimo valor:{limpar}')
            print(f'{verde_claro}NÚMERO = {num}{limpar} > {roxo}lista = [{lista[-1]}]{limpar}')
        lista.append(num)
        print()
    else:
        posição = 0
        while posição < len(lista):
            print(f'{amarelo}Posição = {posição+1}ª{limpar} <=> {amarelo_claro}Quantidade {roxo}lista = {amarelo_claro}{len(lista)}{limpar}')
            print(f'{verde_claro}NÚMERO = {num}{limpar} <= {roxo}lista = [{lista[posição]}]{limpar}')
            if num <= lista[posição]:
                lista.insert(posição, num)
                print(f'{verde}↑ VERDADE ↑{limpar}')
                print()
                break
            print(f'{vermelho_claro}↑ FALSO ↑{limpar}')
            print(f'{roxo}Lista = {lista}{limpar}')
            posição += 1

print(f'Os valores digitados {sub}{amarelo_claro}posto em ordem{limpar} na {roxo}lista = {lista}{limpar}')
