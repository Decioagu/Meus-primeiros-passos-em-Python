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

print(f'{ciano}={limpar}'*33)
print(f'{ciano}={verde_claro} ANALISE DE DADOS EM UMA TUPLA {ciano}={limpar}')
print(f'{ciano}={limpar}'*33)

print()
print(f'Quantas vezes aparece o número {vermelho_claro}9{limpar}?')
print(f'Quais as posições aparce o número {amarelo_claro}3{limpar}?')
print(f'Quais os valores {azul_claro}Pares{limpar} foram digitados?')
cont = fim = 0
print()

n0 = int(input(f'Digite o {verde_claro}primeiro número{limpar}: '))
n1 = int(input(f'Digite o {verde_claro}segundo número{limpar}: '))
n2 = int(input(f'Digite o {verde_claro}terceiro número{limpar}: '))
n3 = int(input(f'Digite o {verde_claro}quarto número{limpar}: '))
tupla = (n0, n1, n2, n3)
print()

print(f'Os números escolidos foram: {verde_claro}{tupla}{limpar}')

if tupla.count(9) <= 1:
    print(f'O valor {vermelho_claro}9{limpar} apareceu {vermelho_claro}{tupla.count(9)} vez{limpar}.')
else:
    print(f'O valor {vermelho_claro}9{limpar} apareceu {vermelho_claro}{tupla.count(9)} vezes{limpar}.')

if 3 in tupla:
    valor = tupla.count(3)
    if valor == 1:
        print(f'O valor {amarelo_claro}3{limpar} apareceu na posição: ', end='')
    else:
        print(f'O valor {amarelo_claro}3{limpar} apareceu nas posições: ', end='')
    for index, v in enumerate(tupla, start=1):
        if v == 3:
            print(f'{amarelo_claro}{index}ª{limpar}', end='')
            cont += 1
            if valor != cont:
                print(end=', ')
            else:
                print('.')
else:
    print(f'O valor {amarelo_claro}3{limpar} não aparece.')

cont = 0
for i in tupla:
    if i % 2 == 0:
        fim +=1
if fim <= 1:
    print(f'O valor {azul_claro}Par{limpar} digitado foi: ', end='')
else:
    print(f'Os valores {azul_claro}Pares{limpar} digitados foram: ', end='')
for c in tupla:
    if c % 2 == 0:
        print(f'{azul_claro}{c}{limpar}', end= '')
        cont += 1
        if cont != fim:
            print(end=', ')
        else:
            print(end='.')
if fim == 0:
    print(f'{azul_claro}0{limpar}')
print()


