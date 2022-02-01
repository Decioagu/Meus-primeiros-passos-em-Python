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

print(f'{azul_claro}={limpar}'*37)
print(f'{azul_claro}={verde_claro} LISTA COMPOSTA E ANÁLISE DE DADOS {azul_claro}={limpar}')
print(f'{azul_claro}={limpar}'*37)
#print(len('Lista composta e análise de dados')+4)

print()
cont = contpesomax = contpesomin = pesomax = pesomin = 0
opção = ''
cadastro = []
pessoa = []

#LOOP DE CADASTRAMENTO
while opção != 'N':
    while True:
        cont += 1
        print(f' {roxo}{cont}º CADASTRO{limpar} '.center(45, '='))
        nome = input(f'{amarelo_claro}Nome{limpar}: ').strip().upper()
        pessoa.append(nome)
        while True:
            peso = input(f'{amarelo_claro}Peso{limpar}: ').strip()
            peso_x = peso
            if peso_x.count('.') <= 1:
                peso_x = peso_x.replace('.', '')
                if peso_x.isnumeric() == True:
                    peso = float(peso)
                    pessoa.append(peso)
                    break
                else:
                    print(f'{vermelho}Caracter invalido!{limpar}')
                    print(f'{amarelo_claro}Favor digitar apenas valores númericos separados por um unico {vermelho_claro}"{amarelo_claro}.{vermelho_claro}" {amarelo_claro}para valores decinamais.{limpar}')
            else:
                print(f'{amarelo_claro}Favor digitar apenas valores númericos separados por um unico {vermelho_claro}"{amarelo_claro}.{vermelho_claro}" {amarelo_claro}para valores decinamais.{limpar}')
        cadastro.append(pessoa[:])
        pessoa.clear()
        break

    #MARCADORES DE PESO MAXIMO E MINIMO
    if cont == 1:
        pesomax = pesomin = peso
    else:
        if pesomax < peso:
            pesomax = peso
        if pesomin > peso:
            pesomin = peso

    #CONTINUAÇÃO DO LOOP
    while True:
        opção = input(f'Quer continuar? [{amarelo_claro}S{limpar}/{amarelo_claro}N{limpar}] ').upper()
        if opção in 'S':
            print()
            break
        elif opção in 'N':
            cont = 0
            break
        else:
            print(f'{vermelho_claro}Opção invalida!{limpar}')
            print(f'Digite "{amarelo_claro}S{limpar}" para {amarelo_claro}CONTINUAR{limpar} ou "{amarelo_claro}N{limpar}" para {amarelo_claro}SAIR{limpar}.')

#CONTADORES DE PESO MAXIMO E MINIMO
for c in cadastro:
    if c[1] == pesomax:
        contpesomax += 1
for c in cadastro:
    if c[1] == pesomin:
        contpesomin += 1

print()
#RESPOSTAS PARA UM CADASTRAMENTO
if len(cadastro) == 1:
    print(f'Ao todo foi cadsatrado apenas {amarelo_claro}{len(cadastro)} pessoa{limpar}.')
    print(f'{amarelo_claro}{cadastro[0][0]}{limpar} pesa {amarelo_claro}{cadastro[0][1]:.2f}Kg{limpar}.')
else:
    print(f'Ao todo foram cadsatradas {amarelo_claro}{len(cadastro)} pessoas{limpar}.')
    if pesomin == pesomax:
        print(f'Todos pesam {amarelo_claro}{pesomax:.2f}Kg{limpar}.')
    else:
        if contpesomax == 1:
            print(f'O {vermelho_claro}MAIOR{limpar} peso foi de ', end='')
        else:
            print(f'O {amarelo_claro}MAIOR{limpar} peso foram de ', end='')

        for c in cadastro:
            if c[1] == pesomax:
                print(f'{vermelho_claro}{c[0]}{limpar}', end='')
                cont += 1
                if cont == contpesomax:
                    print(' ', end='')
                elif cont == contpesomax - 1:
                    print(' e ', end='')
                else:
                    print(', ', end='')
        print(f'pesando {vermelho_claro}{pesomax:.2f}Kg{limpar}.')

        cont = 0
        if contpesomin == 1:
            print(f'O {amarelo_claro}MENOR{limpar} peso foi de ', end='')
        else:
            print(f'O {amarelo_claro}MENOR{limpar} peso foram de ', end='')
        for c in cadastro:
            if c[1] == pesomin:
                print(f'{amarelo_claro}{c[0]}{limpar}', end='')
                cont += 1
                if cont == contpesomin:
                    print(' ', end='')
                elif cont == contpesomin - 1:
                    print(' e ', end='')
                else:
                    print(', ', end='')
        print(f'pesando {amarelo_claro}{pesomin:.2f}Kg{limpar}.')




