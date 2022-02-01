import cor


def título(txt):
    """
    Formata texto em um padrão em caixa

    :param txt: Variável em texto para formatar
    :return: Retorna texto formatado
    """
    print(f'{cor.ciano_claro}={cor.limpar}' * (len(txt) + 4))
    print(f'{cor.ciano_claro}= {cor.roxo}{txt} {cor.ciano_claro}={cor.limpar}')
    print(f'{cor.ciano_claro}={cor.limpar}' * (len(txt) + 4))
