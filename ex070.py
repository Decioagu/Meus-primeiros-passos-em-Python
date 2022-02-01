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

from time import sleep
preco = total = maisde1000 = maisbarato = cont = 0
opcao = nome = nomemaisbarato = ''

print('{}{}'.format(f'{ciano}+-'*15, f'+{limpar}'))
print('{}{:♥^39}{}'.format(vermelho_claro,f'{azul} lOJAS DESCONTÃO {vermelho_claro}',limpar))
print('{}{}'.format(f'{ciano}+-'*15, f'+{limpar}'))
print()

while True:
    cont +=1
    print('{}{}{}'.format(verde_claro,'{:=^40}',limpar).format(f'{ciano_claro}{cont}º COMPRA{verde_claro}'))

    nome = input('Nome do produto: ').strip().upper()
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        maisde1000 += 1
    if cont == 1 or maisbarato > preco:
        maisbarato = preco
        nomemaisbarato = nome

    opcao = input(f'Você quer continuar [{amarelo_claro}S{limpar}/{amarelo_claro}N{limpar}]?').strip().upper()
    while not opcao in 'SN':
        print(f'{vermelho_claro}Opção invalida!{limpar}')
        sleep(1)
        print()
        print(f'Digite "{amarelo_claro}S{limpar}" para {amarelo_claro}Sim{limpar} ou "{amarelo_claro}N{limpar}" para {amarelo_claro}Não{limpar}.')
        opcao = input(f'Você quer continuar [{amarelo_claro}S{limpar}/{amarelo_claro}N{limpar}]?').strip().upper()
    if opcao == 'N':
        print()
        break
    print()

print(f'{ciano}={limpar}'*60)
if cont == 1:
    print(f'Total da compra foi {amarelo}R${total:.2f}{limpar}')
else:
    print('Total das compras foi {1}R${2:.2f}{0}'.format(limpar, amarelo, total))
if maisde1000 == 1:
    print(f'Tem {amarelo}{maisde1000}{limpar} produto custado mais de R$1000.')
else:
    print(f'Temos {amarelo}{maisde1000}{limpar} produtos custando mais de R$1000.')
print('O produto mais barato foi {1}{2}{0} que custa {1}R$:{3:.2f}{0}'.format(limpar, amarelo, nomemaisbarato, maisbarato))
print(f'{ciano}={limpar}' * 60)
