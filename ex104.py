# TABELA DE CORES
limpar = '\033[m'
roxo = '\033[35m'
vermelho_claro = '\033[91m'
verde_claro = '\033[92m'
amarelo_claro = '\033[93m'
azul_claro = '\033[94m'
sub = '\033[4m'
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


def leiaInt(num):
    """
    Testa caractere e permanece em loop infinito até usuário
    digitar um número inteiro de qualquer valor

    :param num: Variável testada
    :return: Retorna somente valores numéricos inteiros
    """
    while True:
        teste = str(input(num))
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
                print(
                    f'{amarelo_claro}Favor digitar apenas valores {sub}numéricos inteiros{limpar}{amarelo_claro}.{limpar}')
                print()
    return num


# ___Main___
titulo('Validando entrada de dados em Python'.upper())
print()
n = leiaInt(f'Digite um {verde_claro}{sub}número inteiro{limpar}: ')
print(f'Você acabou de digitar o número {verde_claro}{n}{limpar} => ({verde_claro}Tipo{limpar} = {verde_claro}{type(n)}{limpar}).')
