limpa = '\033[m'
preto = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'
cinza = '\033[37m'
sub = '\033[4m'
neg = '\033[1m'
inv = '\033[7m'
x = 'S'
num = maior = menor = media = cont = soma = 0
print()
while x != 'N':
    num = input('Digite um número: ')
    cont += 1
    if num.isnumeric() == True:
        num = int(num)
        if cont == 1:
            maior = menor = num
    else:
        while num.isnumeric() == False:
            print()
            print('{}Caracter invalido!{}'.format(vermelho, limpa))
            num = input('Digite um número: ')
        num = int(num)
        if cont == 1:
            maior = menor = num
    soma += num
    if maior < num:
        maior = num
    if menor > num:
        menor = num
    x = input('Quer continuar? [{1}S{0}/{2}N{0}]'.format(limpa, verde, amarelo)).strip().upper()
    if not x in 'SN':
        while not x in 'SN':
            print()
            print('Caracter invalido!'.format(vermelho, limpa))
            print('Digite "{1}S{0}" para {1}continuar{0} ou "{2}N0}" para {2}sair{0}.'.format(limpa, verde, amarelo))
            x = input('Quer continuar? [{1}S{0}/{2}N{0}'.format(limpa, verde, amarelo)).strip().upper()

media = soma/cont
if cont <= 1:
    print()
    print('Você digitou apenas {1}{2}{0} número.'.format(limpa, verde, cont))
    print('Não haverá {1}média{0} ou {1}comparação{0} dos valores'.format(limpa, roxo))
else:
    print()
    print('Você digitou {1}{3}{0} números e a {2}média{0} foi {2}{4}{0}'.format(limpa, verde, roxo, cont, media))
    if maior == menor:
        print('Todos os valores digitados foram {1}{2}{0}.'.format(limpa, roxo, num))
    else:
        print('O {1}maior{0} valor foi {1}{3}{0} e o {2}menor{0} foi {2}{4}{0}.'.format(limpa, azul, amarelo, maior,menor))
