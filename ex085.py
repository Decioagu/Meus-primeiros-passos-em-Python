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

print(f'{azul_claro}={limpar}'*30)
print(f'{azul_claro}={verde_claro} Listas com pares e ímpares {azul_claro}={limpar}')
print(f'{azul_claro}={limpar}'*30)
#print(len('Listas com pares e ímpares')+4)

lista = [[], []]
print()
for c in range(1,8):
    while True:
        num = input(f'Digite o {amarelo}{c}º{limpar} valor: ').strip()
        if num.isnumeric() == True:
            num = int(num)
            break
        else:
            print(f'{vermelho_claro}Caracter invalido!{limpar}')
            print(f'{amarelo_claro}Favor digitar apenas valores númericos inteiros.{limpar}')
            print()
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()

print()
if len(lista[0]) == 1:
    print(f'O valor {azul_claro}PAR{limpar} digitado foi: {azul_claro}{lista[0]}{limpar}')
elif len(lista[0]) == 0:
    print(f'Não há valor {azul_claro}PAR{limpar} digitado.')
else:
    print(f'Os valores {azul_claro}PARES{limpar} digitados foram: {azul_claro}{lista[0]}{limpar}')

if len(lista[1]) == 1:
    print(f'O valor {roxo}IMPAR{limpar} digitado foi: {roxo}{lista[1]}{limpar}')
elif len(lista[1]) == 0:
    print(f'Não há valor {roxo}IMPAR{limpar} digitado.')
else:
    print(f'Os valores {roxo}IMPARES{limpar} digitados foram: {roxo}{lista[1]}{limpar}')



