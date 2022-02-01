# TABELA DE CORES
limpar = '\033[m'
roxo = '\033[35m'
vermelho_claro = '\033[91m'
verde_claro = '\033[92m'
amarelo_claro = '\033[93m'
azul_claro = '\033[94m'
sub = '\033[4m'
neg = '\033[1m'
# FIM DA TABELA DE CORES


def titulo(txt):
    """
    Formata texto em um padrão em caixa

    :param txt: Variável em texto para formatar
    :return: Retorna texto formatado
    """
    print(f'{azul_claro}={limpar}' * (len(txt) + 4))
    print(f'{azul_claro}= {roxo}{txt} {azul_claro}={limpar}')
    print(f'{azul_claro}={limpar}' * (len(txt) + 4))


def teste_int(num):
    """
    Testa caractere e permanece em loop infinito até usuário
    digitar um número inteiro de qualquer valor

    :param num: Variável testada
    :return: Retorna somente valores numéricos inteiros
    """
    teste = num
    while True:
        if teste.count('-') == 1:
            teste = teste.replace('-', '')
            if teste.isnumeric():
                teste = '-' + teste
                num = int(teste)
                break
        else:
            if teste.isnumeric():
                num = int(teste)
                break
            elif teste == '':
                print(end='')
            else:
                print(f'{vermelho_claro}Erro...{limpar}')
                print(f'{amarelo_claro}Favor digitar apenas valores {sub}numéricos inteiros{limpar}{amarelo_claro}.{limpar}')
                print()
            teste = input(f'Digite um valor {sub}{verde_claro}numérico inteiro{limpar}: ').strip()
    return num


def fatorial(n, show=True):
    """
    Calcula o fatorial de um número

    :param n: Variável recebida "valor"
    :param show: (Opcional) Mostra o calculo fatorial
    :return: Não tem retorno loop infinito até "n" receber valor inteiro e negativo

    Programa finaliza ao digitar um valor inteiro negativo
    """
    n = teste_int(n)
    while n >= 0:
        fator = 1
        print(f'{roxo}{n}!{limpar}={azul_claro} ', end='')
        for cont in range(n, 0, -1):
            if show:
                print(f'{cont}', end='')
                if cont > 1:
                    print(end=' x ')
                else:
                    print(end=f' {limpar}= ')
            fator = fator * cont

        print(f'{verde_claro}{fator}{limpar}')
        print(f'Para {amarelo_claro}SAIR{limpar} do programa digite qualquer {amarelo_claro}NÚMERO NEGATIVO{limpar}!')
        print()
        n = input(f'Digite um {sub}{verde_claro}número inteiro{limpar} para fatorar: ')
        n = teste_int(n)

# ___Main___
titulo('Função para Fatorial'.upper())
print(f'''
{roxo}Fatorial{limpar} é um {sub}{verde_claro}número natural inteiro positivo{limpar}, representado 
por “{roxo}n!{limpar}”, que é obtido a partir da multiplicação de todos
os seus antecessores até chegar a número "1". 

{neg}{amarelo_claro}Onde{limpar}: {roxo}n!{limpar} = {azul_claro}n x {limpar}({azul_claro}n – 1{limpar}) {azul_claro} x {limpar} ({azul_claro}n – 2{limpar}) {azul_claro} x {limpar} ({azul_claro}n – 3{limpar}){azul_claro}...{limpar} 

{neg}{amarelo_claro}Ex{limpar}:
{roxo}0!{limpar} = {verde_claro}1{limpar}
{roxo}1!{limpar} = {verde_claro}1{limpar}
{roxo}2!{limpar} = {azul_claro}2 x 1 {limpar}= {verde_claro}2{limpar}{azul_claro}
{roxo}3!{limpar} = {azul_claro}3 x 2 x 1 {limpar}= {verde_claro}6{limpar}
{roxo}4!{limpar} = {azul_claro}4 x 3 x 2 x 1 {limpar}= {verde_claro}24{limpar}
{roxo}5!{limpar} = {azul_claro}5 x 4 x 3 x 2 x 1 {limpar}= {verde_claro}120{limpar}
{roxo}6!{limpar} = {azul_claro}6 x 5 x 4 x 3 x 2 x 1 {limpar}= {verde_claro}720{limpar}
{roxo}7!{limpar} = {azul_claro}7 x 6 x 5 x 4 x 3 x 2 x 1 {limpar}= {verde_claro}5040{limpar}
{roxo}8!{limpar} = {azul_claro}8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 {limpar}= {verde_claro}40320{limpar}
{roxo}9!{limpar} = {azul_claro}9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 {limpar}= {verde_claro}362880{limpar}
{roxo}10!{limpar} = {azul_claro}10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 {limpar}= {verde_claro}3628800{limpar}''')
print()
valor = input(f'Digite um {sub}{verde_claro}número inteiro{limpar} para fatorar: ')
fatorial(valor)
print()
print(f'{vermelho_claro}Fim...{limpar}')








