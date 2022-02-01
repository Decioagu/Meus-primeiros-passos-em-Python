# TABELA DE CORES
limpar = '\033[m'
roxo = '\033[35m'
vermelho_claro = '\033[91m'
verde_claro = '\033[92m'
amarelo_claro = '\033[93m'
azul_claro = '\033[94m'
# FIM DA TABELA DE CORES


def aumentar(valor):
    aumento = valor / 10
    valor += aumento
    return valor


def diminuir(valor):
    valor = valor - (valor * 10)/100
    return valor


def dobro(valor):
    valor *= 2
    return valor


def metade(valor):
    valor /= 2
    return valor

def teste_float(num):
    """
    Testa caractere e permanece em loop infinito até usuário
    digitar um valor numérico valido

    :param num: Variável testada
    :return: Retorna valores numéricos validos
    """
    while True:
        teste = num
        if num == '':
            print(end='')
            num = input(f'Digite o preço: {verde_claro}R${limpar}').strip()
        else:
            if teste.count('.') <= 1:
                teste = teste.replace('.', '')
                if teste.isnumeric() == True:
                    num = float(num)
                    break
                else:
                    print()
                    print(f'{vermelho_claro}Erro...{limpar}')
                    print(f'{amarelo_claro}Caractere digitado não é valido.{limpar}')
                    print()
                    num = input(f'Digite o preço: {verde_claro}R${limpar}').strip()
            else:
                print()
                print(f'{vermelho_claro}Erro...{limpar}')
                print(f'{amarelo_claro}Caractere digitado não é valido.{limpar}')
                print()
                num = input(f'Digite o preço: {verde_claro}R${limpar}').strip()
    return num

def titulo(txt):
    """
    Formata texto em um padrão em caixa

    :param txt: Variável em texto para formatar
    :return: Retorna texto formatado
    """
    print(f'{azul_claro}={limpar}' * (len(txt) + 4))
    print(f'{azul_claro}= {roxo}{txt} {azul_claro}={limpar}')
    print(f'{azul_claro}={limpar}' * (len(txt) + 4))
