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


def leiaint(msg):
    """
    Testa caractere e permanece em loop infinito até usuário
    digitar um número inteiro de qualquer valor

    :param msg: Recebe mensagem para variável "num" que será testada
    :return: Retorna somente valores numéricos inteiros
    """
    while True:
        try:
            num = input(msg).strip()
            teste = int(num)
        except ValueError:
            print()
            print(f'{vermelho_claro}Erro...{limpar}')
            print(f'{amarelo_claro}Caractere "{vermelho_claro}{num}{amarelo_claro}" não é valido.{limpar}')
            continue
        return teste


def leiafloat(msg, alternativa_str=True):
    """
    Testa caractere e permanece em loop infinito até usuário
    digitar um valor numérico valida. Variável testada pode ser
    escrita por "." ou "," exemplo: "4.29" ou "4,29"

    :param msg: Recebe mensagem para variável "num" que será testada
    :param alternativa_str: Quando "True", retorna "return num"
    de tipo 'int' para tipo 'str'.
    :return: Retorna valores numéricos validos 'int' ou formatado como 'str',
    se "alternativa_str=True"
    """
    while True:
        try:
            num = input(msg).strip()
            entrada_num = num
            num = num.replace(',', '.')
            teste = float(num)
        except (ValueError):
            print()
            print(f'Erro...')
            print(f'Caractere "{entrada_num}" não é valido.')
            continue
        if alternativa_str:
            return f'{num}'.replace('.', ',') if entrada_num.count(',') == 1 else num
        else:
            return teste


titulo('Funções aprofundadas em Python'.upper())
inteiro = leiaint(f'Digite um {verde_claro}{sub}número inteiro{limpar}: ')
real = leiafloat(f'Digite um {verde_claro}{sub}número real{limpar}: ')
print(f'O {verde_claro}{sub}valor inteiro{limpar} {verde_claro}= {inteiro}{limpar} e o {verde_claro}{sub}valor real{limpar} {verde_claro}= {real}{limpar}')