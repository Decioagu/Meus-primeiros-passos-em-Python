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

print(f'{azul_claro}={limpar}'*43)
print(f'{azul_claro}={verde_claro} ACRESCENTAR VALORES ÚNICOS EM UMA LISTA {azul_claro}={limpar}')
print(f'{azul_claro}={limpar}'*43)
#print(len('ACRESCENTAR VALORES ÚNICOS EM UMA LISTA'))

print()
opção = ''
lista = []
while opção != 'N':
    while True:
        valor = input('Digite uma valor: ')
        if valor.isnumeric() == True:
            valor = int(valor)
            if valor not in lista:
                print(f'{verde_claro}Valor adiciona com sucesso!{limpar}')
                lista.append(valor)
                break
            else:
                print(f'Valor {amarelo_claro}DUPLICADO{limpar}! {vermelho_claro}NÃO será adicionado...{limpar}')
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
lista.sort()
if len(lista) == 1:
    print(f'Você digitou o valor {verde_claro}{lista}{limpar}')
else:
    print(f'Você digitou os valores {verde_claro}{lista}{limpar}')