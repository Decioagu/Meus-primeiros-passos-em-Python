import COR


def titulo(txt):
    """
    Formata texto em um padrão em caixa

    :param txt: Variável em texto para formatar
    :return: Retorna texto formatado
    """
    print(f'{COR.ciano_claro}={COR.limpar}' * (len(txt) + 4))
    print(f'{COR.ciano_claro}= {COR.roxo}{txt} {COR.ciano_claro}={COR.limpar}')