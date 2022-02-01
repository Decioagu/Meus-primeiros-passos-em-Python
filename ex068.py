limpa = '\033[m'
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
cyan_claro = '\033[96m'
branco = '\033[97m'
sub = '\033[4m'
neg = '\033[1m'
inv = '\033[7m'

print('{1}{2}{3}{0}'.format(limpa, rosa,'+-'*15,'+'))
print(f'Vamos Jogar "{verde}Par{limpa}" ou "{azul}Impar{limpa}"!!!')
print('{1}{2}{3}{0}'.format(limpa, rosa,'+-'*15,'+'))
print()

from random import randint
from time import  sleep

jogador = soma = cont = 0
opcao = valor = ''

while True:
    computador = randint(0,10)
    #print('Colinha:',computador)

    jogador = input(f'{cinza}Digite um número inteiro{limpa}: ')
    if jogador.isnumeric() == True:
        jogador = int(jogador)
    else:
        while jogador.isnumeric() == False:
            print()
            print(f'{amarelo}Digite apenas valores númericos inteiros...{limpa}')
            sleep(0.5)
            jogador = input(f'{cinza}Digite um número inteiro{limpa}:  ')
        jogador = int(jogador)

    opcao = input(f'Escolha "{verde}Par{limpa}" ou "{azul}Impar{limpa}"? [{verde}P{limpa}/{azul}I{limpa}]').strip().upper()
    while opcao not in 'PI':
        print(f'{vermelho}Opção invalida!{limpa}')
        sleep(1)
        print()
        print(f'Digite "{verde}P{limpa}" para {verde}Par{limpa} ou "{azul}I{limpa}" para {azul}Impar{limpa}...')
        opcao = input(f'Escolha "{verde}Par{limpa}" ou "{azul}Impar{limpa}"? [{verde}P{limpa}/{azul}I{limpa}]').strip().upper()
    print()
    if opcao == 'P':
        print(f'{verde_claro}Você escolheu{limpa} "{verde}Par{limpa}"...')
    else:
        print(f'{verde_claro}Você escolheu{limpa} "{azul}Impar{limpa}"...')

    soma = jogador + computador
    if soma % 2 == 0:
        valor = f'{verde}Par{limpa}'
        teste = 'P'
        s = f'{verde}{soma}{limpa}'
    else:
        valor = f'{azul}Impar{limpa}'
        teste = 'I'
        s = f'{azul}{soma}{limpa}'
    print()
    print('{1}{2}{3}{0}'.format(limpa, roxo,'+-'*32,'+'))
    print(f'{verde_claro}Você{limpa} jogou {verde_claro}{jogador}{limpa} e o {vermelho}computador{limpa} jogou {vermelho}{computador}{limpa}. Total da soma é {s}, "{valor}"!')
    print('{1}{2}{3}{0}'.format(limpa, roxo,'+-'*32,'+'))

    if opcao == teste:
        print()
        print(f'{verde}Você VENCEU!!!{limpa}')
        print(f'{amarelo}Vamos jogar novamente...{limpa}')
        cont += 1
        print()
    else:
        if cont <= 1:
            print()
            print(f'{vermelho_claro}Fim de jogo!{limpa} Você venceu {amarelo_claro}{cont} vez{limpa}.')
            break
        else:
            print()
            print(f'{vermelho_claro}Fim de jogo!{limpa} Você venceu {amarelo_claro}{cont} vezes{limpa}.')
            break
