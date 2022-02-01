limpa = '\033[m'
preto = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'
cinza = '\033[37m'
neg = '\033[1m'
sub = '\033[4m'
inv = '\033[7m'

from time import sleep

opção = ''
menu = 0
while opção != 'FIM':
    print()
    print('{}{}{}'.format(roxo, '{:=^70}', limpa).format('{}DIGITE DOIS VALORES NUMÉRICOS E '
                                                         'ESCOLHA AS OPÇÕES{}').format(ciano, roxo))
    print()
    menu = 0
    n1 = input('Digite o {}primeiro valor{}: '.format(verde, limpa)).strip()
    if n1.isnumeric() == True:
        n1 = int(n1)
    else:
        while n1.isnumeric() == False:
            print('{}Digite apenas valores numéricos...{}'.format(amarelo, limpa))
            n1 = input('Digite o {}{}primeiro valor{}: '.format(verde, sub, limpa)).strip()
            print()
        n1 = int(n1)
    n2 = input('Digite o {}segundo valor{}: '.format(ciano, limpa)).strip()
    if n2.isnumeric() == True:
        n2 = int(n2)
    else:
        while n2.isnumeric() == False:
            print('{}Digite apenas valores numéricos...{}'.format(amarelo, limpa))
            n2 = input('Digite o {}{}segundo valor{}: '.format(ciano, sub, limpa)).strip()
            print()
        n2 = int(n2)
    print()
    while not 3 < menu < 6:
        opção = ''
        print()
        print('Escolha alguma {}opção{} abaixo:'.format(ciano, limpa))
        print('{2}[{1}1{2}]{0} = {1}Soma{0}'.format(limpa, roxo, ciano))
        print('{2}[{1}2{2}]{0} = {1}Multiplicar{0}'.format(limpa, amarelo, ciano))
        print('{2}[{1}3{2}]{0} = {1}O maior número{0}'.format(limpa, vermelho, ciano))
        print('{2}[{1}4{2}]{0} = {1}Escolher novos valores{0}'.format(limpa, azul, ciano))
        print('{2}[{1}5{2}]{0} = {1}Sair do programa{0}'.format(limpa, verde, ciano))
        opção = input('Digite a {}opção{} desejada:'.format(ciano, limpa)).strip()
        if opção.isnumeric() == True:
            menu = int(opção)
            if not 0 < menu < 6:
                print('{}Opção invalida!{}'.format(vermelho, limpa))
                sleep(2)
            if menu == 1:
                print()
                print('{}Soma:{}'.format(roxo, limpa))
                print('{1}{4}{0} + {2}{5}{0} = {3}{6}{0}'.format(limpa, verde, ciano, roxo, n1, n2, n1 + n2))
            if menu == 2:
                print()
                print('{}Multiplica{}:'.format(amarelo, limpa))
                print('{1}{4}{0} * {2}{5}{0} = {3}{6}{0}'.format(limpa, verde, ciano, amarelo, n1, n2, n1 * n2))
            if menu == 3:
                print()
                print('{}O maior número{}:'.format(vermelho, limpa))
                if n1 > n2:
                    print('{1}{3} > {2}{4}{0}'.format(limpa, verde, ciano, n1, n2))
                elif n1 < n2:
                    print('{1}{3} {2}< {4}{0}'.format(limpa, verde, ciano, n1, n2))
                else:
                    print('{1}{4}{0} {3}={0} {2}{5}{0}'.format(limpa, verde, ciano, vermelho, n1, n2))
            if menu == 5:
                opção = 'FIM'

        else:
            while opção.isnumeric() == False:
                print('{}Digite apenas valores numéricos...{}'.format(amarelo, limpa))
                opção = '0'
                sleep(2)
                print()
            menu = int(opção)

print()
print('{}Fim do programa...{}'.format(verde, limpa))
