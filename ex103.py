# TABELA DE CORES
limpar = '\033[m'
verde = '\033[32m'
amarelo = '\033[33m'
roxo = '\033[35m'
verde_claro = '\033[92m'
amarelo_claro = '\033[93m'
ciano_claro = '\033[96m'
neg = '\033[1m'
# FIM DA TABELA DE CORES


def titulo(txt):
    """
    Formata texto em um padrão em caixa

    :param txt: Variável em texto para formatar
    :return: Retorna texto formatado
    """
    print(f'{ciano_claro}={limpar}' * (len(txt) + 4))
    print(f'{ciano_claro}= {roxo}{txt} {ciano_claro}={limpar}')
    print(f'{ciano_claro}={limpar}' * (len(txt) + 4))
    print()


def teste_int(num):
    """
    Testa caractere e permanece em loop infinito até usuário
    digitar um número inteiro de qualquer valor

    :param num: Variável testada
    :return: Retorna somente valores numéricos inteiros
    """
    teste = num
    while True:
        if teste.isnumeric():
            num = int(teste)
            break
        elif teste == '':
            num = 0
            break
        else:
            print(f'Erro...')
            print(f'Favor digitar apenas valores numéricos inteiros.')
            print()
        teste = input(f'Digite um valor numérico inteiro: ').strip()
    return num


def ficha(j="DESCONHECIDO", g=0):
    print(f'O {verde}jogador {verde_claro}{neg}{j}{limpar} ', end='')
    if g <=1:
        print(f'fez {amarelo_claro}{g} {amarelo}{neg}gol{limpar} no campeonato.')
    else:
        print(f'fez {amarelo_claro}{g} {amarelo}{neg}gols{limpar} no campeonato.')

titulo('Ficha do Jogador'.upper())
jogador = input(f'Nome do {verde}jogador{limpar}: ').strip()
gol = input(f'Número de {amarelo}gols{limpar} do {verde}jogador{limpar}: ').strip()
gol = teste_int(gol)
print()
if jogador == '':
    ficha(g=gol)
else:
    ficha(jogador, gol)

