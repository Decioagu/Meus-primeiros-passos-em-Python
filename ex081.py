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
cont = 0
opção = ''
lista = []
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
print(f'{roxo}Lista = {lista}{limpar}')

if len(lista) == 1:
    print(f'Você digitou {verde_claro}{len(lista)}{limpar} elemento.')
else:
    print(f'Você digitou {verde_claro}{len(lista)}{limpar} elementos.')

if 5 in lista:
    if lista.count(5) == 1:
        print(f'O {amarelo_claro}número 5{limpar} aparece {amarelo_claro}{lista.count(5)} vez{limpar}, na {amarelo_claro}posição{limpar} ', end='')
    else:
        print(f'O {amarelo_claro}número 5{limpar} aparece {amarelo_claro}{lista.count(5)} vezes{limpar}, nas {amarelo_claro}posições{limpar} ', end='')

cont = 0
for posicao, c in enumerate(lista, start=1):
    if c == 5:
        cont += 1
        print(f'{amarelo_claro}{posicao}º{limpar}', end='')
        if cont == lista.count(5):
            print('.', end='')
        else:
            print(', ', end='')

if len(lista) != 1:
    l = lista[:]
    l.sort(reverse=True)
    print(f'\nO valo da {roxo}LISTA{limpar} em ordem {vermelho_claro}{sub}DECRESCENTE{limpar} é {vermelho_claro}{l}{limpar}')
print()

