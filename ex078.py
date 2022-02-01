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

print(f'{azul_claro}={limpar}'*36)
print(f'{azul_claro}={verde_claro} MAIOR E MENOR VALOR DE UMA LISTA {azul_claro}={limpar}')
print(f'{azul_claro}={limpar}'*36)
print()

contmax = pontuaçãomax = contmin = pontuaçãomin = 0
lista = list()

for núm in range(0,5):
    valor = int(input(f'Digite um valor para {verde_claro}{núm+1}ª{limpar} posição : '))
    lista.append(valor)

print()
print(f'Os valores da {verde_claro}lISTA{limpar} são: {verde_claro}{lista}{limpar}')
maximo = max(lista)
minimo = min(lista)
if maximo == minimo:
    print(f'{azul_claro}TODOS{limpar} os valores digitagos são {azul_claro}IGUAIS{limpar}.')
else:
    # MAIOR VALOR
    for valor in lista:
        if valor == maximo:
            contmax += 1
    if contmax == 1:
        print(f'O {vermelho_claro}MAIOR{limpar} valor digitado foi {vermelho_claro}{maximo}{limpar} na posição ', end='')
    else:
        print(f'O {vermelho_claro}MAIOR{limpar} valor digitado foi {vermelho_claro}{maximo}{limpar} nas posições ', end='')
    for posição, valor in enumerate(lista, start=1):
        if valor == maximo:
            pontuaçãomax += 1
            print(f'{vermelho}{posição}ª{limpar}', end='')
            if pontuaçãomax == contmax:
                print(end='.')

# MENOR VALOR
    print()
    for valor in lista:
        if valor == minimo:
            contmin += 1
    if contmin == 1:
        print(f'O {amarelo_claro}MENOR{limpar} valor digitado foi {amarelo_claro}{minimo}{limpar} na posição ', end='')
    else:
        print(f'O {amarelo_claro}MENOR{limpar} valor digitado foi {amarelo_claro}{minimo}{limpar} nas posições ', end='')
    for posição, valor in enumerate(lista, start=1):
        if valor == minimo:
            pontuaçãomin += 1
            print(f'{amarelo}{posição}ª{limpar}', end='')
            if pontuaçãomin == contmin:
                print(end='.')
print()
