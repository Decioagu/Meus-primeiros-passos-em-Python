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

print(f'='*34)
print('{}{}{}'.center(20, '=').format(amarelo_claro ,' LISTAGEM DE PREÇOS ', limpar))
print(f'='*34)
cont = 0
tupla = ('{:.<25}'.format('Lápis'),'R$','{: 7}'.format(1.75),
'{:.<25}'.format('Borracha'),'R$','{: 7}'.format(2.75),
'{:.<25}'.format('Caderno'),'R$','{: 7}'.format(15.90),
'{:.<25}'.format('Estojo'),'R$','{: 7}'.format(25.00),
'{:.<25}'.format('Transferidor'),'R$','{: 7}'.format(4.20),
'{:.<25}'.format('Compasso'),'R$','{: 7}'.format(9.99),
'{:.<25}'.format('Mochila'),'R$','{: 7}'.format(120.32),
'{:.<25}'.format('Caneta'),'R$','{: 7}'.format(22.30),
'{:.<25}'.format('Livro'),'R$','{: 7}'.format(34.90))
for c in tupla:
    print(c, end='')
    cont += 1
    if cont == 3:
        print()
        cont = 0
print(f'='*34)