# TABELA DE CORES
limpar = '\033[m'
roxo = '\033[35m'
ciano = '\033[36m'
vermelho_claro = '\033[91m'
verde_claro = '\033[92m'
amarelo_claro = '\033[93m'
sub = '\033[4m'
# FIM DA TABELA DE CORES


def titulo(txt):
    """
    Formata texto em um padrão em caixa

    :param txt: Variável em texto para formatar
    :return: Retorna texto formatado
    """
    print(f'{ciano}={limpar}' * (len(txt) + 4))
    print(f'{ciano}= {roxo}{txt} {ciano}={limpar}')
    print(f'{ciano}={limpar}' * (len(txt) + 4))


def teste_int(num):
    """
    Testa caractere e permanece em loop infinito até usuário
    digitar um número inteiro de qualquer valor

    :param num: Variável testada
    :return: Retorna somente valores numéricos inteiros
    """
    while True:
        teste = num
        if num == '':
            print(end='')
            num = input(f'Digite um {verde_claro}{sub}número inteiro{limpar}: ').strip()
        else:
            if teste.count('-') <= 1:
                teste = teste.replace('-', '')
                if teste.isnumeric():
                    num = int(num)
                    break
                else:
                    print()
                    print(f'{vermelho_claro}Erro...{limpar}')
                    print(f'{amarelo_claro}Caractere "{vermelho_claro}{num}{amarelo_claro}" não é valido.{limpar}')
                    num = input(f'Digite um {verde_claro}{sub}número inteiro{limpar}: ').strip()
            else:
                print()
                print(f'{vermelho_claro}Erro...{limpar}')
                print(f'{amarelo_claro}Caractere "{vermelho_claro}{num}{amarelo_claro}" não é valido.{limpar}')
                num = input(f'Digite um {verde_claro}{sub}número inteiro{limpar}: ').strip()
    return num


print()
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
        entrada_num = num
        num = num.replace(',', '.')
        teste = num
        if num == '':
            print(end='')
            num = input(f'Digite um {verde_claro}{sub}número real{limpar}: ').strip()
        else:
            if teste.count('-') <= 1:
                teste = teste.replace('-', '')
                if teste.count('.') <= 1:
                    teste = teste.replace('.', '')
                    if teste.isnumeric() == True:
                        if teste == '0':
                            num = 0
                            num = float(num)
                            break
                        else:
                            num = float(num)
                            break
                    else:
                        print()
                        print(f'{vermelho_claro}Erro...{limpar}')
                        print(f'{amarelo_claro}Caractere "{vermelho_claro}{entrada_num}{amarelo_claro}" não é valido.{limpar}')
                        num = input(f'Digite um {verde_claro}{sub}número real{limpar}: ').strip()
                else:
                    print()
                    print(f'{vermelho_claro}Erro...{limpar}')
                    print(f'{amarelo_claro}Caractere "{vermelho_claro}{entrada_num}{amarelo_claro}" não é valido.{limpar}')
                    num = input(f'Digite um {verde_claro}{sub}número real{limpar}: ').strip()
            else:
                print()
                print(f'{vermelho_claro}Erro...{limpar}')
                print(f'{amarelo_claro}Caractere "{vermelho_claro}{entrada_num}{amarelo_claro}" não é valido.{limpar}')
                num = input(f'Digite um {verde_claro}{sub}número real{limpar}: ').strip()
    return f'{num}'.replace('.', ',') if entrada_num.count(',') == 1 else num


titulo('Funções aprofundadas em Python'.upper())
inteiro = input(f'Digite um {verde_claro}{sub}número inteiro{limpar}: ').strip()
inteiro = teste_int(inteiro)
real = input(f'Digite um {verde_claro}{sub}número real{limpar}: ').strip()
real = teste_float(real)
print(f'O {verde_claro}{sub}valor inteiro{limpar} {verde_claro}= {inteiro}{limpar} e o {verde_claro}{sub}valor real{limpar} {verde_claro}= {real}{limpar}')
