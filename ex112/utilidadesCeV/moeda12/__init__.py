# TABELA DE CORES
limpar = '\033[m'
roxo = '\033[35m'
vermelho_claro = '\033[91m'
verde_claro = '\033[92m'
amarelo_claro = '\033[93m'
azul_claro = '\033[94m'
# FIM DA TABELA DE CORES

def metade(valor):
  res = valor / 2
  return moeda(res)


def dobro(valor):
    res = valor * 2
    return moeda(res)


def aumento(valor, taxa=10):
    res = valor + (valor * taxa)/100
    return moeda(res)


def aumento(valor, taxa=10):
    res = valor + (valor * taxa)/100
    return moeda(res)


def redução(valor, taxa=10):
    res = valor - (valor * taxa)/100
    return moeda(res)


def moeda(valor, moeda='R$'):
    """
    Formata na impressão um Valor Numérico em Moeda
    Ex: Valor Numérico= 3.50 para Moeda= R$3,50

    :param preço: Valor Numérico a ser formatado
    :param moeda: Adiciona simbolo desejado=> Ex: R$
    :return: Retorna valor formatado em Moeda
    """
    return f'{verde_claro}{moeda}{valor:.2f}{limpar}'.replace('.', ',')


def teste_float(num, formatação=False):
    """
    Testa caractere e permanece em loop infinito até usuário
    digitar um valor numérico valida. Variável testada pode ser
    escrita por "." ou "," exemplo: "4.29" ou "4,29"

    :param num: Variável testada
    :param formatação: Quando "True", retorna "return num"
    de tipo 'int' para tipo 'str'. Exemplo: "3.45" para "3,45"
    :return: Retorna valores numéricos validos 'int' ou formatado como 'str'
    """
    while True:
        num = num.replace(',', '.')
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
                    print(f'{amarelo_claro}Caractere "{vermelho_claro}{num}{amarelo_claro}" não é valido.{limpar}')
                    print()
                    num = input(f'Digite o preço: {verde_claro}R${limpar}').strip()
            else:
                print()
                print(f'{vermelho_claro}Erro...{limpar}')
                print(f'{amarelo_claro}Caractere "{vermelho_claro}{num}{amarelo_claro}" não é valido.{limpar}')
                print()
                num = input(f'Digite o preço: {verde_claro}R${limpar}').strip()
    return num if not formatação else f'{num}'.replace('.', ',')


def titulo(txt):
    """
    Formata texto em um padrão em caixa

    :param txt: Variável em texto para formatar
    :return: Retorna texto formatado
    """
    print(f'{azul_claro}={limpar}' * (len(txt) + 4))
    print(f'{azul_claro}= {roxo}{txt} {azul_claro}={limpar}')
    print(f'{azul_claro}={limpar}' * (len(txt) + 4))


def resumo(valor, taxaa=10, taxar=10):
    titulo('RESUMO DOS VALORES'.center(27))
    print(f'Preço analisado: {moeda(valor)}')
    print(f'{azul_claro}-{limpar}' * 31)
    print(f'Preço {roxo}metade{limpar}: {metade(valor)}')
    print(f'Preço {roxo}dobro{limpar}: {dobro(valor)}')
    print(f'Preço {roxo}aumento{limpar} de {amarelo_claro}{taxaa}%{limpar}: {moeda(valor + (valor * taxaa)/100)}')
    print(f'Preço {roxo}redução{limpar} de {amarelo_claro}{taxar}%{limpar}: {moeda(valor - (valor * taxar)/100)}')
    print(f'{azul_claro}-{limpar}' * 31)

