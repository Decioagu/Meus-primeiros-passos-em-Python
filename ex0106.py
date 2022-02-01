# TABELA DE CORES
limpar = '\033[m'
roxo = '\033[35m'
vermelho_claro = '\033[91m'
verde_claro = '\033[92m'
amarelo_claro = '\033[93m'
amarelo_claro = '\033[93m'
azul_claro = '\033[94m'
amarelo = '\033[30:43m'

# FIM DA TABELA DE CORES

from time import sleep


def titulo(txt):
    f"""
    {verde_claro}Formata texto em um padrão em caixa

    :param txt: Variável em texto para formatar
    :return: Retorna texto formatado{limpar}
    """
    print(f'{azul_claro}={limpar}' * (len(txt) + 4))
    print(f'{azul_claro}= {roxo}{txt} {azul_claro}={limpar}')
    print(f'{azul_claro}={limpar}' * (len(txt) + 4))


def ajuda():
    while True:
        sleep(0.5)
        print(f'{azul_claro}Sistema de ajuda PyHELP{limpar}')
        sleep(1)
        x = input(f'{verde_claro}Função ou biblioteca =>{limpar} ')
        sleep(0.5)
        if x.upper() == 'FIM':
            print(f'{vermelho_claro}Fim...{limpar}')
            break
        else:
            print(f'Acessando o manual do comando "{amarelo_claro}{x}{limpar}"')
            sleep(1)
            print(amarelo, end='')
            help(x)
            print(limpar, end='')


# ___Main___
titulo('Interactive helping system in Python'.upper())
print()
ajuda()

