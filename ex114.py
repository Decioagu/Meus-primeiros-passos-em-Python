import COR
import urllib.request


def titulo(txt):
    """
    Formata texto em um padrão em caixa

    :param txt: Variável em texto para formatar
    :return: Retorna texto formatado
    """
    print(f'{COR.ciano_claro}={COR.limpar}' * (len(txt) + 4))
    print(f'{COR.ciano_claro}= {COR.roxo}{txt} {COR.ciano_claro}={COR.limpar}')
    print(f'{COR.ciano_claro}={COR.limpar}' * (len(txt) + 4))


titulo('Site está acessível?'.upper())
print()
try:
    site = urllib.request.urlopen('https://www.youtube.com')
    print(f'https://www.youtube.com')
    print()
except urllib.error.URLError:
    print(f'{COR.vermelho_claro}O site não esta acessível, verifique sua conexão.{COR.limpar}')
else:
    print(f'{COR.verde_claro}O site esta acessível.{COR.limpar}')




