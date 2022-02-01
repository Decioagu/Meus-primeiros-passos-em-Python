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
# FIM TABELA DE CORES

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'quatorze', 'quaize', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
opcao = ''

while True:
    n = int(input(f'Digite um número entre {verde_claro}0{limpar} e {verde_claro}20{limpar}: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {verde_claro}{cont[n]}{limpar}')
        opcao = input(f'Você quer continuar [{amarelo_claro}S{limpar}/{amarelo_claro}N{limpar}]? ').strip().upper()
        print()
        while not opcao in 'SN':
            print(f'{vermelho_claro}Opção invalido!{limpar}')
            print(f'Digite "{amarelo_claro}S{limpar}" para {amarelo_claro}continuar{limpar} ou "{amarelo_claro}N{limpar}" para {amarelo_claro}parar{limpar}.')
            opcao = input(f'Você quer continuar [{amarelo_claro}S{limpar}/{amarelo_claro}N{limpar}]? ').strip().upper()
            print()
        if opcao == 'N':
            break
    else:
        print(f'{vermelho_claro}Valor invalido!{limpar}')
        print()
print(f'{roxo}Fim...{limpar}')


